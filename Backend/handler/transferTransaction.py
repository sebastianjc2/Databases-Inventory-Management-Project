from Backend.DAOs.transferTransaction import TransferTransactionDAO
from Backend.DAOs.warehouse_dao import WarehouseDAO
from Backend.DAOs.parts import PartDAO
from Backend.DAOs.user_dao import UserDAO
from Backend.DAOs.stored_in import StoredInDAO
from Backend.DAOs.racks import RackDAO
from flask import jsonify


class TransferTransactionHandler:
    def __init__(self):
        self.transferTransactionDAO = TransferTransactionDAO()
        self.warehouse_dao = WarehouseDAO()
        self.user_dao = UserDAO()
        self.part_dao = PartDAO()
        self.stored_in_dao = StoredInDAO()
        self.rack_dao = RackDAO()
    
    def mapToDict(self, tup):
        my_dict = {}
        my_dict["transferID"] = tup[0]
        my_dict["transactionDate"] = tup[1]
        my_dict["partAmount"] = tup[2]
        my_dict["toWarehouse"] = tup[3]
        my_dict["userRequester"] = tup[4]
        my_dict["transactionID"] = tup[5]
        my_dict["partID"] = tup[6]
        my_dict["userID"] = tup[7]
        my_dict["warehouseID"] = tup[8]
        return my_dict


    def addTransferTransaction(self, data):
        try:
            transactionDate = data["transactionDate"]
            partAmount = data["partAmount"]
            toWarehouse = data["toWarehouse"]
            userRequester = data["userRequester"]
            partID = data["partID"]
            warehouseID = data["warehouseID"]
            userID = data["userID"]
        except KeyError as e:
            return jsonify({"Invalid argument names!": e.args}), 400
        
        # Check that all fields are integers.
        for key in data:
                if key != "transactionDate" and not isinstance(data[key],int):
                    return jsonify(Error='{} has to be a integer.'.format(key)), 400
        
        # Verify types
        if not isinstance(data["transactionDate"],str):
            return jsonify(Error='{} has to be a string.'.format("transactionDate")), 400
        elif partAmount <= 0:
            return jsonify("partAmount must be a positive number greater than 0"), 400
        elif not self.user_dao.getUserByID(userID):
            return jsonify("Invalid Tranfer. The user who sent the transfer does not exist."), 400
        elif not self.user_dao.getUserByID(userRequester):
            return jsonify("Invalid Transfer. The user who requested the transfer does not exist."), 400
        elif not self.part_dao.searchByID(partID):
            return jsonify("Invalid Transfer. The part does not exist."), 400
        elif not self.warehouse_dao.getWarehouseByID(warehouseID):
            return jsonify("Invalid Transfer. The warehouse who sent the transfer does not exist."), 400
        elif not self.warehouse_dao.getWarehouseByID(toWarehouse):
            return jsonify("Invalid Transfer. The warehouse that requested the warehouse does not exist."), 400
        elif not self.warehouse_dao.worksIn(warehouseID, userID):
            return jsonify("Invalid Transfer. The user who sent the transfer does not work in the warehouse that "
                           "will be sending the transfer."), 400
        elif not self.warehouse_dao.worksIn(toWarehouse, userRequester):
            return jsonify("Invalid Transfer. The user who requested the transfer does not work in the warehouse that "
                           "will be receiving the transfer."), 400


        # Verify that the relationship exists in stored_in
        sender_rackID = self.stored_in_dao.get_rack_with_pid_wid(warehouseID, partID)
        if not sender_rackID:
            return jsonify(f"There is no rack for source warehouse ({warehouseID}) and part ({partID})"), 400

        # Make sure theres enough parts to send
        sender_parts_total = self.stored_in_dao.get_quantity(wid=warehouseID, pid=partID, rid=sender_rackID)
        if sender_parts_total < partAmount:
            return jsonify(
                "Invalid Transfer. The sender warehouse does not have enough parts to send ({sender_parts_total})."
                ), 400
                
        # Make sure the destination has a rack that accepts the given part 
        new_rack_rid = self.stored_in_dao.get_rack_with_pid_wid(toWarehouse, partID)
        if not new_rack_rid:
            return jsonify(f"There is no rack for destination warehouse ({toWarehouse}) and part ({partID})"), 400

        # update part quantity in destination
        to_warehouse_total = self.stored_in_dao.get_quantity(wid=toWarehouse, pid=partID, rid=new_rack_rid)
        flag = self.stored_in_dao.modify_quantity(toWarehouse, partID, new_rack_rid, to_warehouse_total + partAmount)
        if not flag: return jsonify(Error="Internal Server Error: Failed to modify destination quantity"), 500

        # Update part quantity of the sender warehouse
        flag = self.stored_in_dao.modify_quantity(warehouseID, partID, sender_rackID, sender_parts_total - partAmount)
        if not flag: return jsonify(Error="Internal Server Error: Failed to modify source quantity"), 500

        transferid = self.transferTransactionDAO.addTransferTransaction(
                                                    to_warehouse=toWarehouse,
                                                    user_requester=userRequester,
                                                    tdate=transactionDate,
                                                    part_amount=partAmount,
                                                    pid=partID,
                                                    uid=userID,
                                                    wid=warehouseID)
        
        if transferid:
            data["transferid"] = transferid
            return jsonify(data), 201
        return jsonify("Internal Server Error: TRONKA"), 500

    
    def getAllTransferTransaction(self):
        dao = TransferTransactionDAO()
        dbtuples = dao.getAllTransferTransaction()
        if dbtuples:
            result = []
            for tup in dbtuples:
                result.append(self.mapToDict(tup))
            return jsonify(result)
        else:
            return jsonify("Internal Server Error"), 500
    

    def getTransferTransactionById(self, transferid):
        dao = TransferTransactionDAO()
        dbtuples = dao.getTransferTransactionById(transferid)
        if dbtuples:
            result = []
            for tup in dbtuples:
                result.append(self.mapToDict(tup))
            return jsonify(result)
        else:
            return jsonify("Transfer {} does not exist".format(transferid)), 400


    def modifyTransferTransactionByID(self, transferid, data):
        try:
            transactionDate = data["transactionDate"]
            partAmount = data["partAmount"]
            toWarehouse = data["toWarehouse"]
            userRequester = data["userRequester"]
            partID = data["partID"]
            warehouseID = data["warehouseID"]
            userID = data["userID"]
        except KeyError as e:
            return jsonify({"Unexpected attribute values": e.args}), 400
        
        if partAmount < 0:
            return jsonify("partAmount must be a positive number"), 400

        if (transactionDate and partAmount and partID and warehouseID and userID):
            dao = TransferTransactionDAO()
            flag = dao.modifyTransferTransactionById(to_warehouse=toWarehouse,
                                                     user_requester=userRequester,
                                                     tdate=transactionDate,
                                                     part_amount=partAmount,
                                                     pid=partID,
                                                     uid=userID,
                                                     wid=warehouseID,
                                                     transferid=transferid)
            if flag:
                return jsonify(data), 200
            else:
                return jsonify("Not Found"), 404
        else:
            return jsonify("Attributes cannot contain null fields."), 400
