from flask import jsonify
from Backend.DAOs.parts import PartDAO


class PartHandler:
    """
    this should:
    * connect to the DB
    * extract the list of parts
    * take those records,
    * and make them a JSON
    """
    def getAllParts_old(self):
        result = []
        result.append({'id': 2, 'name': 'tuerca','color': 'blue'})
        result.append({'id': 4, 'name': 'clavo','color': 'gray'})
        return jsonify(result)

    def mapToDict(self, tup):
        # this is kind of getting hardcoded, because we have to know the order in which we want the query
        # tuples are every record, so this just maps the records into dictionaries
        # if the query changes, we have to change mapToDict. We have to have a constructor for each class
        my_dict = {}
        my_dict['id'] = tup[0]
        my_dict['Name'] = tup[1]
        my_dict['Color'] = tup[2]
        my_dict['Material'] = tup[3]
        my_dict['msrp'] = tup[4]
        return my_dict

    def getAllParts(self):
        dao = PartDAO()
        # data access object: design pattern that captures, in an object, the query to be sent to the DB
        dbtuples = dao.getAllParts()  # this should return an array of Tuples

        result = []
        # loop thru each tuple and turn them into a dictionary (serialization)
        for tup in dbtuples:
            result.append(self.mapToDict(tup))
        return jsonify(result)

    def searchByID(self, pid):
        dao = PartDAO()
        result = dao.searchByID(pid)  # if this is null, then the part with that id doesn't exist
        if result:
            return jsonify(self.mapToDict(result))
        else:
            return jsonify("Not Found"), 404

    def insertPart(self, data):
        # print(data)

        # looking up the values in the dict
        name = data['Name']
        color = data['Color']
        material = data['Material']
        msrp = data['msrp']

        if name and color and material and msrp:
            dao = PartDAO()
            pid = dao.insertPart(name, color, material, msrp)
            data['pid'] = pid
            return jsonify(data), 201
        else:
            return jsonify("Unexpected attribute values."), 400

    def deleteByID(self, pid):
        dao = PartDAO()
        result = dao.deleteByID(pid)  # if this is null, then the part with that id doesn't exist
        if result:
            return jsonify(f"Deleted part with id: {pid}"), 200
        else:
            return jsonify("Not Found"), 404

    def updateByID(self, pid, data):
        # looking up the values in the dict
        name = data['Name']
        color = data['Color']
        material = data['Material']
        msrp = data['msrp']

        if pid and name and color and material and msrp:
            dao = PartDAO()
            flag = dao.updateByID(pid, name, color, material, msrp)
            if flag:
                return jsonify(data), 200
            else:
                return jsonify("Not Found"), 404
        else:
            return jsonify("Unexpected attribute values."), 400
