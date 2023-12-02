from Backend.DAOs.outgoingTransaction import OutgoingTransactionDAO
from Backend.DAOs.stored_in import StoredInDAO
from Backend.DAOs.warehouse_dao import WarehouseDAO
from Backend.DAOs.user_dao import UserDAO
from flask import jsonify


class OutgoingTransactionHandler:
    def mapToDict(self, tup):
        my_dict = {}
        my_dict["otid"] = tup[0]
        my_dict["tdate"] = tup[1]
        my_dict["unit_sale_price"] = tup[2]
        my_dict["part_amount"] = tup[3]
        my_dict["cid"] = tup[4]
        my_dict["tid"] = tup[5]
        my_dict["pid"] = tup[6]
        my_dict["uid"] = tup[7]
        my_dict["wid"] = tup[8]
        return my_dict


    def addOutgoingTransaction(self, data):
        try:
            transactionDate = data["transactionDate"]
            partAmount = data["partAmount"]
            unitSalePrice = data["unitSalePrice"]
            partID = data["partID"]
            warehouseID = data["warehouseID"]
            customerID = data["customerID"]
            userID = data["userID"]
        except KeyError as e:
            return jsonify(Error={"Unexpected parameter names": e.args}), 400
        
        # Verify nulls
        if not (transactionDate and partAmount and unitSalePrice and partID
                and warehouseID and customerID and userID):
            return jsonify(Error="Attributes cannot contain null fields."), 400

        # Verify types
        for attr in (partID, warehouseID, customerID, userID, partAmount):
            if not isinstance(attr, int):
                return jsonify(Error=f"Invalid attritube for type 'int' ({attr})"), 400
        if not isinstance(unitSalePrice, float) and not isinstance(unitSalePrice, int):
            return jsonify(Error=f"Invalid type for unitBuyPrice ({unitSalePrice})"), 400
        if not isinstance(transactionDate, str):
            return jsonify(Error=f"Invalid type for transaction date ({transactionDate})"), 400


        # Verify user is in warehouse
        tuple = UserDAO().getUserByID(uid=userID)
        if not tuple: return jsonify(Error=f"Internal server error: Failed to get user with id {userID}"), 500
        warehouse_for_user = tuple[0][6]
        if warehouse_for_user != warehouseID:
            return jsonify(Error=f"User ({userID}) works at warehouse {warehouse_for_user}, not {warehouseID}"), 400


        # Verify values are valid
        if unitSalePrice < 0:
            return jsonify(Error="unitSalePrice must be a positive number"), 400
        if partAmount < 0:
            return jsonify(Error="partAmount must be a positive number"), 400
        
        # Get the rid for the warehouse and part
        stored_in_DAO = StoredInDAO()
        rackID = stored_in_DAO.get_rack_with_pid_wid(wid=warehouseID, pid=partID)
        if not rackID:
            return jsonify(Error=f"No rack assigned to warehouse ({warehouseID}) and part ({partID})"), 400

        # Verify against quantity in warehouse
        available_quantity = stored_in_DAO.get_quantity(wid=warehouseID, pid=partID, rid=rackID)
        if available_quantity < partAmount:
            return jsonify(Error=f"Not enough stock ({available_quantity}) in warehouse ({warehouseID})"), 400

        # Add transaction
        otid = OutgoingTransactionDAO().addOutgoingTransaction(unit_sale_price=unitSalePrice,
                                                               cid=customerID,
                                                               tdate=transactionDate,
                                                               part_amount=partAmount,
                                                               pid=partID,
                                                               uid=userID,
                                                               wid=warehouseID)
        if not otid: return jsonify(Error="Failed to add transaction"), 500

        # Update available budget
        revenue = partAmount*unitSalePrice
        new_budget = WarehouseDAO().increase_budget(wid=warehouseID, delta=revenue)
        if not new_budget: return jsonify(Error="Failed to update warehouse budget"), 500

        # Update stored_in
        quantity_delta = available_quantity - partAmount
        count = stored_in_DAO.modify_quantity(wid=warehouseID, pid=partID, rid=rackID, new_quantity=quantity_delta)
        if not count:
            return jsonify(Error=
                f"Failed to modify quantity of part ({partID}) in warehouse ({warehouseID})"
                ), 500

        data["otid"] = otid
        return jsonify(Result=data), 201

    
    def getAllOutgoingTransaction(self):
        dao = OutgoingTransactionDAO()
        dbtuples = dao.getAllOutgoingTransaction()
        if dbtuples:
            result = []
            for tup in dbtuples:
                result.append(self.mapToDict(tup))
            return jsonify(Result=result)
        else:
            return jsonify(Error="Failed to load transactions"), 500
    

    def getOutgoingTransactionById(self, otid):
        dao = OutgoingTransactionDAO()
        dbtuples = dao.getOutgoingTransactionById(otid)
        if dbtuples:
            return jsonify(Result=self.mapToDict(dbtuples[0]))
        else:
            return jsonify(Error="Could not find matching outgoing transaction"), 500