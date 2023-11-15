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
        name = data['name']
        country = data['country']
        city = data['city']
        street = data['street']
        zipcode = data['zipcode']
        phone = data['phone']

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
            return jsonify("Not Found"), 404

    def deleteByID(self, sid):
        dao = SupplierDAO()
        res = dao.deleteByID(sid)
        if res:
            return jsonify(f'Deleted part with id: {sid}'), 200
        else:
            return jsonify("Not Found"), 404

    def updateByID(self, sid, data):
        name = data['name']
        country = data['country']
        city = data['city']
        street = data['street']
        zipcode = data['zipcode']
        phone = data['phone']

        if sid and name and country and city and street and zipcode and phone:
            dao = SupplierDAO()
            flag = dao.updateByID(sid, name, country, city, street, zipcode, phone)
            if flag:
                return jsonify(data), 200
            else:
                return jsonify("Not Found"), 404
        else:
            return jsonify("Unexpected attribute values."), 400
