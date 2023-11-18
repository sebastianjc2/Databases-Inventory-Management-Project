from Backend.DAOs.transferTransaction import TransferTransactionDAO
from flask import jsonify


class TransferTransactionHandler:
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
            return jsonify({"Unexpected attribute values": e.args}), 400
        
        if partAmount < 0:
            return jsonify("partAmount must be a positive number"), 400

        if (transactionDate and partAmount and partID and warehouseID and userID):
            dao = TransferTransactionDAO()
            transferid = dao.addTransferTransaction(to_warehouse=toWarehouse,
                                                    user_requester=userRequester,
                                                    tdate=transactionDate,
                                                    part_amount=partAmount,
                                                    pid=partID,
                                                    uid=userID,
                                                    wid=warehouseID)
            if transferid:
                data["transferid"] = transferid
                return jsonify(data), 201
            else:
                return jsonify("Internal Server Error"), 500
        return jsonify("Attributes cannot contain null fields."), 400

    
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
            return jsonify("Internal Server Error"), 500


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
