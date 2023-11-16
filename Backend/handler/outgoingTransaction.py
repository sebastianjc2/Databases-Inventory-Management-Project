from Backend.DAOs.outgoingTransaction import OutgoingTransactionDAO
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
            return jsonify({"Unexpected attribute values": e.args}), 400
        
        if unitSalePrice < 0:
            return jsonify("unitSalePrice must be a positive number"), 400
        if partAmount < 0:
            return jsonify("partAmount must be a positive number"), 400

        no_values_are_none = (transactionDate and partAmount and unitSalePrice and partID
                              and warehouseID and customerID and userID)

        if no_values_are_none:
            dao = OutgoingTransactionDAO()
            otid = dao.addOutgoingTransaction(unit_sale_price=unitSalePrice,
                                              cid=customerID,
                                              tdate=transactionDate,
                                              part_amount=partAmount,
                                              pid=partID,
                                              uid=userID,
                                              wid=warehouseID)
            if otid:
                data["otid"] = otid
                return jsonify(data), 201
            else:
                return jsonify("Internal Server Error"), 500
        return jsonify("Attributes cannot contain null fields."), 400

    
    def getAllOutgoingTransaction(self):
        dao = OutgoingTransactionDAO()
        dbtuples = dao.getAllOutgoingTransaction()
        if dbtuples:
            result = []
            for tup in dbtuples:
                result.append(self.mapToDict(tup))
            return jsonify(result)
        else:
            return jsonify("Internal Server Error"), 500
    

    def getOutgoingTransactionById(self, otid):
        dao = OutgoingTransactionDAO()
        dbtuples = dao.getOutgoingTransactionById(otid)
        if dbtuples:
            return jsonify(dbtuples)
        else:
            return jsonify("Internal Server Error"), 500


    def modifyOutgoingTransactionByID(self, otid, data):
        try:
            transactionDate = data["transactionDate"]
            partAmount = data["partAmount"]
            unitSalePrice = data["unitSalePrice"]
            partID = data["partID"]
            warehouseID = data["warehouseID"]
            customerID = data["customerID"]
            userID = data["userID"]
        except KeyError as e:
            return jsonify({"Unexpected attribute values": e.args}), 400
        
        if unitSalePrice < 0:
            return jsonify("unitSalePrice must be a positive number"), 400
        if partAmount < 0:
            return jsonify("partAmount must be a positive number"), 400

        no_values_are_none = (transactionDate and partAmount and unitSalePrice and partID
                              and warehouseID and customerID and userID)

        if no_values_are_none:
            dao = OutgoingTransactionDAO()
            flag = dao.modifyOutgoingTransactionById(unit_sale_price=unitSalePrice,
                                                     cid=customerID,
                                                     tdate=transactionDate,
                                                     part_amount=partAmount,
                                                     pid=partID,
                                                     uid=userID,
                                                     wid=warehouseID,
                                                     otid=otid)
            if flag:
                return jsonify(data), 200
            else:
                return jsonify("Not Found"), 404
        else:
            return jsonify("Attributes cannot contain null fields."), 400
