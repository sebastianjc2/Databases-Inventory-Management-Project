from Backend.DAOs.incomingTransaction import IncomingTransactionDAO
from flask import jsonify


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
            return jsonify({"Unexpected attribute values": e.args}), 400
        
        if unitBuyPrice < 0:
            return jsonify("unitBuyPrice must be a positive number"), 400
        if partAmount < 0:
            return jsonify("partAmount must be a positive number"), 400

        no_values_are_none = (transactionDate and partAmount and unitBuyPrice and partID
                              and warehouseID and rackID and supplierID and userID)

        if no_values_are_none:
            dao = IncomingTransactionDAO()
            itid = dao.addIncomingTransaction(unit_buy_price=unitBuyPrice,
                                              sid=supplierID,
                                              rid=rackID,
                                              tdate=transactionDate,
                                              part_amount=partAmount,
                                              pid=partID,
                                              uid=userID,
                                              wid=warehouseID)
            if itid:
                data["itid"] = itid
                return jsonify(data), 201
            else:
                return jsonify("Internal Server Error"), 500
        return jsonify("Attributes cannot contain null fields."), 400

    
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
