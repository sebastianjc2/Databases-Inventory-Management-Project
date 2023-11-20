from Backend.DAOs.transaction import TransactionDAO
from flask import jsonify


class TransactionHandler:
    def mapToDict(self, tup):
        my_dict = {}
        my_dict["tid"] = tup[0]
        my_dict["tdate"] = tup[1]
        my_dict["part_amount"] = tup[2]
        my_dict["pid"] = tup[3]
        my_dict["uid"] = tup[4]
        my_dict["wid"] = tup[5]
        return my_dict



    
    def getAllTransactions(self):
        dao = TransactionDAO()
        dbtuples = dao.getAllTransactions()
        if dbtuples:
            result = []
            for tup in dbtuples:
                result.append(self.mapToDict(tup))
            return jsonify(result)
        else:
            return jsonify("Internal Server Error: Failed to load transactions"), 500
    

    def getTransactionById(self, tid):
        dao = TransactionDAO()
        dbtuples = dao.getTransactionByID(tid)
        if dbtuples:
            result = []
            for tup in dbtuples:
                result.append(self.mapToDict(tup))
            return jsonify(result)
        else:
            return jsonify("Failed to find matching transaction"), 404