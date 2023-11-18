from Backend.DAOs.racks import RackDAO
from Backend.DAOs.parts import PartDAO
from Backend.DAOs.warehouse_dao import WarehouseDAO
from Backend.DAOs.stored_in import StoredInDAO
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
        if len(data) != 5:
            return jsonify("Did not receive the correct amount of information needed for a Rack record. Need the "
                           "following data: rack name (name), capacity, the warehouse id (wid) of the warehouse where "
                           "the rack will be stored, a part id (pid) for the part that the rack will hold and the " 
                           "quantity (qty) of this part that the rack will hold (can't be bigger than its capacity)."
                           ), 400

        try:
            name = data["Name"]
            capacity = data["Capacity"]
            wid = data["wid"]
            pid = data["pid"]
            parts_qty = data["qty"]
        except:
            return jsonify("Error: Invalid argument names!"), 400

        if not isinstance(name, str):
            return jsonify(f"Error: The inputted name '{name}' is not a string!"), 400
        if not isinstance(capacity, int):
            return jsonify(f"Error: The inputted capacity '{capacity}' is not a valid integer!"), 400
        if capacity <= 0:
            return jsonify(f"Error: The rack must have a capacity bigger than 0."), 400
        if not isinstance(wid, int):
            return jsonify(f"Error: The inputted warehouse id '{wid}' is not a valid integer!"), 400
        if not isinstance(pid, int):
            return jsonify(f"Error: The inputted part id '{pid}' is not a valid integer!"), 400
        if not isinstance(parts_qty, int):
            return jsonify(f"Error: The inputted part quantity '{parts_qty}' is not a valid integer!"), 400
        if parts_qty > capacity:
            return jsonify(f"Error: The amount of parts that this rack will hold ({parts_qty}) can't be bigger than "
                           f"its capacity ({capacity})"), 400

        part_exists = PartDAO().searchByID(pid)
        if not part_exists:
            return jsonify(f"Error: The inputted part id '{pid}' is not found in the database."), 400

        warehouse_exists = WarehouseDAO().getWarehouseByID(wid)
        if not warehouse_exists:
            return jsonify(f"Error: The inputted warehouse id '{wid}' is not found in the database."), 400

        # is part already in this warehouse?
        part_in_warehouse = StoredInDAO().isPartInWarehouse(pid, wid)
        if part_in_warehouse:
            return jsonify(f"Error: Part {pid} is already in Warehouse {wid}, and there can only be 1 of the same part "
                           f"per Warehouse"), 400

        if name and capacity:
            dao = RackDAO()

            # does the name already exist?
            name_exists = dao.name_exists(name)
            if name_exists: # it would violate UNIQUE constraint, so give an error
                return jsonify("Error: This name already exists. Please pick another one."), 400

            rid = dao.addRack(name, capacity)
            data['rid'] = rid
            # if everything above went right, we have to add this record to the stored_in table
            StoredInDAO().modify_quantity_or_insert(wid, pid, rid, parts_qty)
            return jsonify(data), 201
        else:
            return jsonify("Unexpected attribute values."), 400

    def getRackByID(self, rid):
        dao = RackDAO()
        tups = dao.getRackById(rid)
        if tups:
            return jsonify(self.mapToDict(tups))
        else:
            return jsonify(f"Could not find a rack with id: {rid}"), 404

    def deleteByID(self, rid):
        dao = RackDAO()

        stores_parts = dao.stores_parts(rid)
        if stores_parts:
            return jsonify("Cannot delete this rack, since it is currently storing parts in it."), 400

        in_transaction = dao.in_incoming_transaction(rid)
        if in_transaction:
            return jsonify("Cannot delete this rack, since it is being referenced in a transaction."), 400

        res = dao.deleteRackById(rid)
        if res:
            return jsonify(f'Deleted rack with id: {rid}'), 200
        else:
            return jsonify(f"Could not find a rack with rack id: {rid}"), 404

    def updateByID(self, rid, data):
        if len(data) != 3 and len(data) != 2:
            return jsonify("Error: Did not receive the correct amount of information needed for a Rack record."), 400

        try:
            name = data['Name']
            capacity = data['Capacity']
        except:
            return jsonify("Error: Invalid argument names!"), 400

        if not isinstance(name, str):
            return jsonify(f"Error: The inputted name '{name}' is not a string!"), 400
        if not isinstance(capacity, int):
            return jsonify(f"Error: The inputted capacity '{capacity}' is not an integer!"), 400

        # check how many parts is this rack currently holding
        qty = StoredInDAO().get_qty_with_rid(rid)
        if capacity < qty:
            return jsonify(f"Error: Cannot update capacity since this new capacity ({capacity}) is less than the amount"
                           f" of parts that this rack is currently holding ({qty}). New capacity must be more than "
                           f"{qty}."), 400

        if rid and name and capacity:
            dao = RackDAO()
            flag = dao.modifyRackById(rid, name, capacity)
            if flag:
                return jsonify(data), 200
            else:
                return jsonify(f"Could not find a rack with rack id: {rid}"), 404
        else:
            return jsonify("Unexpected attribute values."), 400
