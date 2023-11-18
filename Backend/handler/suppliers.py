from flask import jsonify
from Backend.DAOs.suppliers import SupplierDAO


class SupplierHandler:
    def mapToDict(self, tup):
        my_dict = {}
        my_dict['id'] = tup[0]
        my_dict['name'] = tup[1]
        my_dict['country'] = tup[2]
        my_dict['city'] = tup[3]
        my_dict['street'] = tup[4]
        my_dict['zipcode'] = tup[5]
        my_dict['phone'] = tup[6]
        return my_dict

    def getAllSuppliers(self):
        dao = SupplierDAO()

        tups = dao.getAllSuppliers()
        res = []

        for tup in tups:
            res.append(self.mapToDict(tup))
        return jsonify(res)

    def insertSupplier(self, data):
        if len(data) != 6:
            return jsonify("Did not receive the correct amount of information needed for a Supplier record."), 400

        try:
            name = data['name']
            country = data['country']
            city = data['city']
            street = data['street']
            zipcode = data['zipcode']
            phone = data['phone']
        except:
            return jsonify("Error: Invalid argument names!"), 400

        if not isinstance(name, str):
            return jsonify(f"Error: The inputted name '{name}' is not a string!"), 400
        if not isinstance(country, str):
            return jsonify(f"Error: The inputted country '{country}' is not a string!"), 400
        if not isinstance(city, str):
            return jsonify(f"Error: The inputted city '{city}' is not a string!"), 400
        if not isinstance(street, str):
            return jsonify(f"Error: The inputted street name '{street}' is not a string!"), 400
        if not isinstance(zipcode, str):
            return jsonify(f"Error: The inputted zipcode '{zipcode}' is not a string!"), 400
        if not isinstance(phone, str):
            return jsonify(f"Error: The inputted phone number '{phone}' is not a string!"), 400

        if name and country and city and street and zipcode and phone:
            dao = SupplierDAO()
            sid = dao.insertSupplier(name, country, city, street, zipcode, phone)
            data['sid'] = sid
            return jsonify(data), 201
        else:
            return jsonify("Unexpected attribute values."), 400

    def searchByID(self, sid):
        dao = SupplierDAO()
        res = dao.searchByID(sid)
        if res:
            return jsonify(self.mapToDict(res))
        else:
            return jsonify("Did not find a supplier with id:", sid), 404

    def deleteByID(self, sid):
        dao = SupplierDAO()

        supplies_parts = dao.suppliesParts(sid)
        if supplies_parts:
            print("test2")
            return jsonify("Cannot delete this supplier, since it currently supplies parts."), 400

        # Can't delete a part that is being referenced in a transaction
        in_transaction = dao.inTransaction(sid)
        if in_transaction:
            print("test1")
            return jsonify("Cannot delete this supplier, since it is being referenced in a past transaction."), 400

        res = dao.deleteByID(sid)
        if res:
            return jsonify(f'Deleted supplier with id: {sid}'), 200
        else:
            return jsonify("Did not find a supplier with id:", sid), 404

    def updateByID(self, sid, data):
        if len(data) != 6 and len(data) != 7:
            return jsonify("Did not receive the correct amount of information needed for a Supplier record."), 400

        try:
            name = data['name']
            country = data['country']
            city = data['city']
            street = data['street']
            zipcode = data['zipcode']
            phone = data['phone']
        except:
            return jsonify("Error: Invalid argument names!"), 400

        if not isinstance(name, str):
            return jsonify(f"Error: The inputted name '{name}' is not a string!"), 400
        if not isinstance(country, str):
            return jsonify(f"Error: The inputted country '{country}' is not a string!"), 400
        if not isinstance(city, str):
            return jsonify(f"Error: The inputted city '{city}' is not a string!"), 400
        if not isinstance(street, str):
            return jsonify(f"Error: The inputted street name '{street}' is not a string!"), 400
        if not isinstance(zipcode, str):
            return jsonify(f"Error: The inputted zipcode '{zipcode}' is not a string!"), 400
        if not isinstance(phone, str):
            return jsonify(f"Error: The inputted phone number '{phone}' is not a string!"), 400

        if sid and name and country and city and street and zipcode and phone:
            dao = SupplierDAO()
            flag = dao.updateByID(sid, name, country, city, street, zipcode, phone)
            if flag:
                return jsonify(data), 200
            else:
                return jsonify("Did not find a supplier with id:", sid), 404
        else:
            return jsonify("Unexpected attribute values."), 400
