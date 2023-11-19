from flask import jsonify
from Backend.DAOs.supplies import SuppliesDao


class SuppliesHandler:
    def mapToDict(self, tup):
        my_dict = {}
        my_dict['sid'] = tup[0]
        my_dict['pid'] = tup[1]
        my_dict['stock'] = tup[2]
        return my_dict

    def mapPartsSupplied(self, tup):
        my_dict = {}
        my_dict['pid'] = tup[0]
        my_dict['Part Name'] = tup[1]
        my_dict['Part Color'] = tup[2]
        my_dict['Part Material'] = tup[3]
        my_dict['MSRP'] = tup[4]
        my_dict['sid'] = tup[5]
        my_dict['stock'] = tup[6]
        return my_dict
    def getPartsSupplied(self):
        dao = SuppliesDao()

        tups = dao.get_parts_supplied()
        res = []

        for tup in tups:
            res.append(self.mapPartsSupplied(tup))
        return jsonify(res)
