from Backend.DAOs.incomingTransaction import IncomingTransactionDAO
from Backend.DAOs.stored_in import StoredInDAO
from Backend.DAOs.supplies import SuppliesDao
from Backend.DAOs.warehouse_dao import WarehouseDAO
from Backend.DAOs.racks import RackDAO
from Backend.DAOs.user_dao import UserDAO
from flask import jsonify

from Backend.handler.user_handler import UserHandler


class IncomingTransactionHandler:
    def mapToDict(self, tup):
        my_dict = {}
        my_dict["itid"] = tup[0]
        my_dict["tdate"] = tup[1]
        my_dict["unit_buy_price"] = tup[2]
        my_dict["part_amount"] = tup[3]
        my_dict["sid"] = tup[4]
        my_dict["rid"] = tup[5]
        my_dict["tid"] = tup[6]
        my_dict["pid"] = tup[7]
        my_dict["uid"] = tup[8]
        my_dict["wid"] = tup[9]
        return my_dict


    def addIncomingTransaction(self, data):
        try:
            transactionDate = data["transactionDate"]
            partAmount = data["partAmount"]
            unitBuyPrice = data["unitBuyPrice"]
            partID = data["partID"]
            warehouseID = data["warehouseID"]
            rackID = data["rackID"]
            supplierID = data["supplierID"]
            userID = data["userID"]
        except KeyError as e:
            return jsonify({"Unexpected parameter names": e.args}), 400
        
        # Verify nulls
        if not (transactionDate and partAmount and unitBuyPrice and partID
                and warehouseID and rackID and supplierID and userID):
            return jsonify("Attributes cannot contain null fields."), 400

        # Verify types
        for attr in (partID, warehouseID, rackID, supplierID, userID, partAmount):
            if not isinstance(attr, int):
                return jsonify(f"Invalid attritube for type 'int' ({attr})"), 400
        if not isinstance(unitBuyPrice, float) and not isinstance(unitBuyPrice, int):
            return jsonify(f"Invalid type for unitBuyPrice ({unitBuyPrice})"), 400
        if not isinstance(transactionDate, str):
            return jsonify(f"Invalid type for transaction date ({transactionDate})"), 400

        # Verify values are valid
        if unitBuyPrice < 0:
            return jsonify("unitBuyPrice must be a positive number"), 400
        if partAmount < 0:
            return jsonify("partAmount must be a positive number"), 400
        
        # Verify against supplier stock
        supplies_DAO = SuppliesDao()
        stock = supplies_DAO.get_stock_for_part_and_supplier(pid=partID, sid=supplierID)
        if not stock:
            return jsonify(f"Part {partID} not supplied by supplier {supplierID}"), 400
        elif stock < partAmount:
            return jsonify(f"Not enough stock ({stock}) for requested amount ({partAmount})"), 400

        # Verify against budget
        warehouse_DAO = WarehouseDAO()
        cost = unitBuyPrice*partAmount
        budget = warehouse_DAO.get_warehouse_budget(wid=warehouseID)
        if not budget:
            return jsonify(f"Warehouse {warehouseID} not found"), 404
        elif budget < cost:
            return jsonify(
                f"Warehouse budget (${budget}) not enough to buy {partAmount} unit(s) at ${unitBuyPrice} per unit."
                ), 400

        # Verify user is in warehouse
        tuple = UserDAO().getUserByID(uid=userID)
        if not tuple: return jsonify(f"Internal server error: Failed to get user with id {userID}"), 500
        warehouse_for_user = tuple[0][6]
        if warehouse_for_user != warehouseID:
            return jsonify(f"User ({userID}) works at warehouse {warehouse_for_user}, not {warehouseID}"), 400

        # Verfiy rack exists
        rack_capacity = RackDAO().get_capacity(rid=rackID)
        if not rack_capacity: return jsonify(f"Internal Server Error: Rack {rackID} does not exist"), 500

        # Ensure the rack is not being used for another type of part
        stored_in_DAO = StoredInDAO()
        wid, pid = stored_in_DAO.get_entry_with_rid(rid=rackID)
        if not (wid == warehouseID and pid == partID):
            return jsonify(f"Rack ({rackID}) not assigned to warehouse ({warehouseID}) and part ({partID})"), 400

        # Check that the amount fits
        current_amount_in_rack = stored_in_DAO.get_quantity(wid=warehouseID, pid=partID, rid=rackID)
        rack_delta = rack_capacity - current_amount_in_rack
        if partAmount > rack_delta:
            leftover = rack_delta if rack_delta >= 0 else 0
            return jsonify(
                f"Too many parts ({partAmount}). Rack ({rackID}) can hold {leftover} more parts."
                ), 400
        
        # Add transaction
        itid = IncomingTransactionDAO().addIncomingTransaction(unit_buy_price=unitBuyPrice,
                                                               sid=supplierID,
                                                               rid=rackID,
                                                               tdate=transactionDate,
                                                               part_amount=partAmount,
                                                               pid=partID,
                                                               uid=userID,
                                                               wid=warehouseID)
        if not itid: return jsonify("Internal Server Error: Failed to add transaction"), 500

        # Update available stock
        count = supplies_DAO.decrease_stock(pid=partID, sid=supplierID, delta=partAmount)
        if not count: return jsonify("Internal Server Error: Failed to update stock"), 500
        elif stock - partAmount == 0: supplies_DAO.delete_entry(pid=partID, sid=supplierID)

        # Update available budget
        new_budget = warehouse_DAO.decrease_budget(wid=warehouseID, delta=cost)
        if not new_budget: return jsonify("Internal Server Error: Failed to update warehouse budget"), 500

        # Add to stored_in
        count = stored_in_DAO.modify_quantity(wid=warehouseID,
                                              pid=partID,
                                              rid=rackID,
                                              new_quantity=current_amount_in_rack+partAmount)
        if not count:
            return jsonify(
                f"Internal Server Error: Failed to modify quantity of part ({partID}) in warehouse ({warehouseID})"
                ), 500
        
        data["itid"] = itid
        return jsonify(data), 201

    
    def getAllIncomingTransaction(self):
        dao = IncomingTransactionDAO()
        dbtuples = dao.getAllIncomingTransaction()
        if dbtuples:
            result = []
            for tup in dbtuples:
                result.append(self.mapToDict(tup))
            return jsonify(result)
        else:
            return jsonify("Internal Server Error"), 500
    

    def getIncomingTransactionById(self, itid):
        dao = IncomingTransactionDAO()
        dbtuples = dao.getIncomingTransactionById(itid)
        if dbtuples:
            result = []
            for tup in dbtuples:
                result.append(self.mapToDict(tup))
            return jsonify(result)
        else:
            return jsonify("Internal Server Error"), 500


    def modifyIncomingTransactionByID(self, itid, data):
        try:
            transactionDate = data["transactionDate"]
            partAmount = data["partAmount"]
            unitBuyPrice = data["unitBuyPrice"]
            partID = data["partID"]
            warehouseID = data["warehouseID"]
            rackID = data["rackID"]
            supplierID = data["supplierID"]
            userID = data["userID"]
        except KeyError as e:
            return jsonify({"Unexpected attribute values": e.args}), 400
        
        if unitBuyPrice < 0:
            return jsonify("unitBuyPrice must be a positive number"), 400
        if partAmount < 0:
            return jsonify("partAmount must be a positive number"), 400

        no_values_are_none = (transactionDate and partAmount and unitBuyPrice and partID
                              and warehouseID and rackID and supplierID and userID)

        if no_values_are_none:
            dao = IncomingTransactionDAO()
            flag = dao.modifyIncomingTransactionById(unit_buy_price=unitBuyPrice,
                                                     sid=supplierID,
                                                     rid=rackID,
                                                     tdate=transactionDate,
                                                     part_amount=partAmount,
                                                     pid=partID,
                                                     uid=userID,
                                                     wid=warehouseID,
                                                     itid=itid)
            if flag:
                return jsonify(data), 200
            else:
                return jsonify("Not Found"), 404
        else:
            return jsonify("Attributes cannot contain null fields."), 400
