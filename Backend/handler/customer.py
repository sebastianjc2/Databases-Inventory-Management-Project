from Backend.DAOs.customer import CustomerDAO
from flask import jsonify


class CustomerHandler:
    def mapToDict(self, tup):
        my_dict = {}
        my_dict["id"] = tup[0]
        my_dict["FirstName"] = tup[1]
        my_dict["LastName"] = tup[2]
        my_dict["Zipcode"] = tup[3]
        my_dict["Phone"] = tup[4]
        return my_dict

    def getAllCustomers(self):
        dao = CustomerDAO()
        dbtuples = dao.getAllCustomers()
        result = []
        for tup in dbtuples:
            result.append(self.mapToDict(tup))
        return jsonify(result)

    def addCustomer(self, data):
        fname = data["FirstName"]
        lname = data["LastName"]
        zipcode = data["Zipcode"]
        phone = data["Phone"]

        if fname and lname and zipcode and phone:
            dao = CustomerDAO()
            pid = dao.addCustomer(fname, lname, zipcode, phone)
            data["pid"] = pid
            return jsonify(data), 201
        else:
            return jsonify("Unexpected attribute values."), 400

    def getCustomerById(self, cid):
        dao = CustomerDAO()
        dbtuples = dao.getCustomerById(cid)
        return jsonify(dbtuples)

    def modifyCustomerById(self, cid, data):
        fname = data["FirstName"]
        lname = data["LastName"]
        zipcode = data["Zipcode"]
        phone = data["Phone"]

        if fname and lname and zipcode and phone:
            dao = CustomerDAO()
            flag = dao.modifyCustomerById(fname, lname, zipcode, phone, cid)
            if flag:
                return jsonify(data), 200
            else:
                return jsonify("Not Found"), 404
        else:
            return jsonify("Unexpected attribute values."), 400

    def deleteCustomerById(self, cid):
        dao = CustomerDAO()
        res = dao.deleteCustomerById(str(cid))
        if res:
            return jsonify(f'Deleted part with id: {cid}'), 200
        else:
            return jsonify("Not Found"), 404
