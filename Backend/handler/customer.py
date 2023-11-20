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
        if dbtuples:
            result = []
            for tup in dbtuples:
                result.append(self.mapToDict(tup))
            return jsonify(result)
        else:
            return jsonify("Internal Server Error: Failed to load customers"), 500


    def addCustomer(self, data):
        try:
            fname = data["FirstName"]
            lname = data["LastName"]
            zipcode = data["Zipcode"]
            phone = data["Phone"]
        except KeyError as e:
            return jsonify({"Unexpected attribute values": e.args}), 400

        for attr in (fname, lname, zipcode, phone):
            if not isinstance(attr, str):
                return jsonify(f"Error: Invalid attribute for type 'str': {attr}."), 400

        if fname and lname and zipcode and phone:
            dao = CustomerDAO()
            cid = dao.addCustomer(fname, lname, zipcode, phone)
            if cid:
                data["cid"] = cid
                return jsonify(data), 201
            else:
                return jsonify("Internal Server Error: Failed to add customer"), 500
        else:
            # TODO: add validation and error handling and map to dict 
            return jsonify("Unexpected attribute values."), 400
    


    def getCustomerById(self, cid):
        dao = CustomerDAO()
        dbtuples = dao.getCustomerById(cid)
        if dbtuples:
            result = []
            for tup in dbtuples:
                result.append(self.mapToDict(tup))
            return jsonify(result)
        else:
            return jsonify("Internal Server Error: Could not find matching customer"), 500


    def modifyCustomerById(self, cid, data):
        try:
            fname = data["FirstName"]
            lname = data["LastName"]
            zipcode = data["Zipcode"]
            phone = data["Phone"]
        except KeyError as e:
            return jsonify({"Unexpected attribute values": e.args}), 400

        for attr in (fname, lname, zipcode, phone):
            if not isinstance(attr, str):
                return jsonify(f"Error: Invalid attribute for type 'str': {attr}."), 400


        if fname and lname and zipcode and phone:
            dao = CustomerDAO()
            count = dao.modifyCustomerById(fname, lname, zipcode, phone, cid)
            if count == 0:
                return jsonify(f'No customer with id: {cid}'), 404
            elif count == 1:
                return jsonify(data), 200
            else:
                return jsonify(f"Internal Server Error: Multiple customers matched with id {cid}"), 500
        else:
            return jsonify("Attributes cannot contain null fields."), 400

    def deleteCustomerById(self, cid):
        """ TODO: Add validation (Can't delete if referenced in a transaction)"""
        dao = CustomerDAO()
        count = dao.deleteCustomerById(cid)
        if count == 0:
            return jsonify(f'No customer with id: {cid}'), 404
        elif count == 1:
            return jsonify(f'Deleted customer with id: {cid}'), 200
        else:
            return jsonify(f"Internal Server Error: Multiple customers matched with id {cid}"), 500
