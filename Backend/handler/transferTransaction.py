from Backend.DAOs.transferTransaction import TransferTransactionDAO
from Backend.DAOs.warehouse_dao import WarehouseDAO
from Backend.DAOs.parts import PartDAO
from Backend.DAOs.user_dao import UserDAO
from Backend.DAOs.stored_in import StoredInDAO
from Backend.DAOs.racks import RackDAO
from flask import jsonify


class TransferTransactionHandler:
    def __init__(self):
        self.transferTransactionDAO = TransferTransactionDAO()
        self.warehouse_dao = WarehouseDAO()
        self.user_dao = UserDAO()
        self.part_dao = PartDAO()
        self.stored_in_dao = StoredInDAO()
        self.rack_dao = RackDAO()
    
    def mapToDict(self, tup):
        my_dict = {}
        my_dict["transferID"] = tup[0]
        my_dict["transactionDate"] = tup[1]
        my_dict["partAmount"] = tup[2]
        my_dict["toWarehouse"] = tup[3]
        my_dict["userRequester"] = tup[4]
        my_dict["transactionID"] = tup[5]
        my_dict["partID"] = tup[6]
        my_dict["userID"] = tup[7]
        my_dict["warehouseID"] = tup[8]
        return my_dict


    def addTransferTransaction(self, data):
        try:
            transactionDate = data["transactionDate"]
            partAmount = data["partAmount"]
            toWarehouse = data["toWarehouse"]
            userRequester = data["userRequester"]
            partID = data["partID"]
            warehouseID = data["warehouseID"]
            userID = data["userID"]
            toRack = data["toRack"]
        except KeyError as e:
            return jsonify(Error={"Invalid argument names!": e.args}), 400
        
        # Check that all fields are integers.
        for key in data:
                if key != "transactionDate" and not isinstance(data[key],int):
                    return jsonify(Error='{} has to be a integer.'.format(key)), 400
        
        # Verify types
        if not isinstance(data["transactionDate"],str):
            return jsonify(Error='{} has to be a string.'.format("transactionDate")), 400
        elif partAmount <= 0:
            return jsonify(Error="partAmount must be a positive number greater than 0"), 400
        elif not self.user_dao.getUserByID(userID):
            return jsonify(Error="Invalid Tranfer. The user who sent the transfer does not exist."), 400
        elif not self.user_dao.getUserByID(userRequester):
            return jsonify(Error="Invalid Transfer. The user who requested the transfer does not exist."), 400
        elif not self.part_dao.searchByID(partID):
            return jsonify(Error="Invalid Transfer. The part does not exist."), 400
        elif not self.warehouse_dao.getWarehouseByID(warehouseID):
            return jsonify(Error="Invalid Transfer. The warehouse who sent the transfer does not exist."), 400
        elif not self.warehouse_dao.getWarehouseByID(toWarehouse):
            return jsonify(Error="Invalid Transfer. The warehouse that requested the warehouse does not exist."), 400
        elif not self.warehouse_dao.worksIn(warehouseID, userID):
            return jsonify(Error="Invalid Transfer. The user who sent the transfer does not work in the "
                           "warehouse that will be sending the transfer."), 400
        elif not self.warehouse_dao.worksIn(toWarehouse, userRequester):
            return jsonify(Error="Invalid Transfer. The user who requested the transfer does not work in the "
                           "warehouse that will be receiving the transfer."), 400


        # Verify that the relationship exists in stored_in for the sender
        # Naturally, if it doesn't we can't perform the transfer
        sender_rackID = self.stored_in_dao.get_rack_with_pid_wid(partID, warehouseID)
        if not sender_rackID:
            return jsonify(Error=f"There is no rack for source warehouse ({warehouseID}) and part ({partID})"), 400

        # Make sure theres enough parts to send
        sender_parts_total = self.stored_in_dao.get_quantity(wid=warehouseID, pid=partID, rid=sender_rackID)
        if sender_parts_total < partAmount:
            return jsonify(Error=
                "Invalid Transfer. The sender warehouse does not have enough parts to send ({sender_parts_total})."
                ), 400

        # Verfiy receiver rack exists
        rack_capacity = RackDAO().get_capacity(rid=toRack)
        if not rack_capacity: return jsonify(Error=f"Rack {toRack} does not exist"), 500

        # Ensure the rack is not being used for another type of part
        stored_in_DAO = StoredInDAO()
        result = stored_in_DAO.get_entry_with_rid(rid=toRack)
        # If the entry exists and doesn't match, error
        if result and not (result[0] == toWarehouse and result[1] == partID):
            return jsonify(Error=f"Rack ({toRack}) not assigned to warehouse ({warehouseID}) and part ({partID})"), 400
        rid = stored_in_DAO.get_rack_with_pid_wid(pid=partID, wid=toWarehouse)
        if rid and rid != toRack:
            return jsonify(Error=f"Warehouse ({warehouseID}) and part ({partID}) assigned to rack {rid}, not {toRack}"), 400

        # Update part quantity in destination
        to_warehouse_total = self.stored_in_dao.get_quantity(wid=toWarehouse, pid=partID, rid=toRack)
        flag = self.stored_in_dao.modify_quantity(toWarehouse, partID, toRack, to_warehouse_total + partAmount)
        if not flag: return jsonify(Error="Failed to modify destination quantity"), 500

        # Update part quantity of the sender warehouse
        flag = self.stored_in_dao.modify_quantity(warehouseID, partID, sender_rackID, sender_parts_total - partAmount)
        if not flag: return jsonify(Error="Failed to modify source quantity"), 500

        transferid = self.transferTransactionDAO.addTransferTransaction(
                                                    to_warehouse=toWarehouse,
                                                    user_requester=userRequester,
                                                    tdate=transactionDate,
                                                    part_amount=partAmount,
                                                    pid=partID,
                                                    uid=userID,
                                                    wid=warehouseID)
        
        if transferid:
            data["transferid"] = transferid
            return jsonify(Result=data), 201
        return jsonify(Error="Failed to add transfer transaction"), 500

    
    def getAllTransferTransaction(self):
        dao = TransferTransactionDAO()
        dbtuples = dao.getAllTransferTransaction()
        if dbtuples:
            result = []
            for tup in dbtuples:
                result.append(self.mapToDict(tup))
            return jsonify(Result=result)
        else:
            return jsonify(Error="Failed to load transfer transaction"), 500
    

    def getTransferTransactionById(self, transferid):
        dao = TransferTransactionDAO()
        dbtuples = dao.getTransferTransactionById(transferid)
        if dbtuples:
            return jsonify(Result=self.mapToDict(dbtuples[0]))
        else:
            return jsonify(Error="Transfer {} does not exist".format(transferid)), 400