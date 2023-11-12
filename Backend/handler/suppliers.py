from flask import jsonify
from Backend.DAOs.suppliers import SupplierDAO


class SupplierHandler:

    def mapToDict(self, tup):
        my_dict = {}
        my_dict['id'] = tup[0]
        my_dict['fname'] = tup[1]
        my_dict['lname'] = tup[2]
        my_dict['country'] = tup[3]
        my_dict['city'] = tup[4]
        my_dict['street'] = tup[5]
        my_dict['zipcode'] = tup[6]
        my_dict['phone'] = tup[7]
        return my_dict

    def getAllSuppliers(self):
        dao = SupplierDAO()

        tups = dao.getAllSuppliers()
        res = []

        for tup in tups:
            res.append(self.mapToDict(tup))
        return jsonify(res)

    def insertSupplier(self, data):

        fname = data['fname']
        lname = data['lname']
        country = data['country']
        city = data['city']
        street = data['street']
        zipcode = data['zipcode']
        phone = data['phone']

        if fname and lname and country and city and street and zipcode and phone:
            dao = SupplierDAO()
            sid = dao.insertSupplier(fname, lname, country, city, street, zipcode, phone)
            data['sid'] = sid
            return jsonify(data), 201
        else:
            return jsonify("Unexpected attribute values."), 400
