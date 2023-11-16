from Backend.DAOs.racks import RackDAO
from flask import jsonify


class RackHandler:
    def mapToDict(self, tup):
        my_dict = {}
        my_dict['id'] = tup[0]
        my_dict['Name'] = tup[1]
        my_dict['Capacity'] = tup[2]
        return my_dict

    def getAllRacks(self):
        dao = RackDAO()
        tups = dao.getAllRacks()
        res = []
        for tup in tups:
            res.append(self.mapToDict(tup))
        return jsonify(res)

    def addRack(self, data):
        name = data["Name"]
        capacity = data["Capacity"]

        if name and capacity:
            dao = RackDAO()
            rid = dao.addRack(name, capacity)
            data['rid'] = rid
            return jsonify(data), 201
        else:
            return jsonify("Unexpected attribute values."), 400

    def getRackByID(self, rid):
        dao = RackDAO()
        tups = dao.getRackById(rid)
        if tups:
            return jsonify(self.mapToDict(tups))
        else:
            return jsonify("Not Found"), 404

    '''TODO: add validation (can't delete if there is parts on it)'''
    def deleteByID(self, rid):
        dao = RackDAO()
        res = dao.deleteRackById(rid)
        if res:
            return jsonify(f'Deleted rack with id: {rid}'), 200
        else:
            return jsonify("Not Found"), 404

    def updateByID(self, rid, data):
        name = data['Name']
        capacity = data['Capacity']
        print(rid,name,capacity)

        if rid and name and capacity:
            dao = RackDAO()
            flag = dao.modifyRackById(rid, name, capacity)
            if flag:
                return jsonify(data), 200
            else:
                return jsonify("Not Found"), 404
        else:
            return jsonify("Unexpected attribute values."), 400
