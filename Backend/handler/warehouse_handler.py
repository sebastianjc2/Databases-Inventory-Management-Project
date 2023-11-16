from flask import jsonify
from Backend.DAOs.warehouse_dao import WarehouseDAO


class WarehouseHandler:
    """WarehouseHandler takes care of managing the communication between the
    request and the database for the warehouses route."""
    
    def __init__(self):
        self.warehouseDAO = WarehouseDAO()
    
    def build_warehouse_dict(self,row:tuple) -> dict:
        """Builds dictionary that contains
        all the information from a warehouse.

        Args:
            row (tuple): A record, given as a tuple, from the
        Warehouses table in the database.

        Returns:
            dict: A dictionary that contains all the information mapped to
        the correct keys. This is so that later the dictionary can be 
        transformed into JSON format.
        """
        warehouse_dict = {}
        warehouse_dict['wid'] = row[0]
        warehouse_dict['wname'] = row[1]
        warehouse_dict['wcountry'] = row[2]
        warehouse_dict['wregion'] = row[3]
        warehouse_dict['wcity'] = row[4]
        warehouse_dict['wstreet'] = row[5]
        warehouse_dict['wzipcode'] = row[6]
        warehouse_dict['wbudget'] = row[7]
        return warehouse_dict
        
        
    def getAllWarehouses(self):
        """Returns all warehouses from the Warehouses Table in the database.
    
        Return: JSON object that contains all the warehouses from the Warehouses Table that were found in the database.
        """
        
        all_warehouses_tuples = self.warehouseDAO.getAllWarehouses()
        all_warehouses_result = []
        for record in all_warehouses_tuples:
            all_warehouses_result.append(self.build_warehouse_dict(record))
        return jsonify(Warehouses=all_warehouses_result)
    
    def insertWarehouse(self,data) -> object:
        """Insert a new warehouse in the Warehouses Table in the database.
        
        Keyword arguments:
        argument: Data to be sent to the DAO.
        Return: JSON object that contains the warehouse ID that was inserted.
        """

        warehouse_name = data['wname']
        warehouse_country = data['wcountry']
        warehouse_region = data['wregion']
        warehouse_city = data['wcity']
        warehouse_street = data['wstreet']
        warehouse_zipcode = data['wzipcode']
        warehouse_budget = data['wbudget']
        
        if warehouse_name and warehouse_country and warehouse_region and warehouse_city \
        and warehouse_street and warehouse_zipcode and (warehouse_budget and warehouse_budget >= 0):
            
            wid = self.warehouseDAO.insertWarehouse(warehouse_name,warehouse_country,warehouse_region,warehouse_city,
                                                    warehouse_street,warehouse_zipcode,warehouse_budget)
            data['wid'] = wid
            return jsonify(data), 201
        else:
            return jsonify(Error='Unexpected attribute values'), 400
        
    def getWarehouseById(self,wid:int) -> object:
        """Execute a query to get a warehouse from the Warehouses Table in the database with the given ID.

        Args:
            wid (_type_): _description_

        Returns:
            _type_: JSON object that contains all the data found of the warehouse with the given ID.
        """
        warehouse_tuple = self.warehouseDAO.getWarehouseByID(wid)
        if not warehouse_tuple:
            return jsonify(Error='Warehouse Not Found'), 404
        else:
            warehouse = self.build_warehouse_dict(warehouse_tuple[0])
            return jsonify(Warehouse=warehouse)
    
    def updateWarehouseByID(self,wid:int,data:object) -> object:
        """Update a warehouse in the Warehouses Table in the database by the given ID.

        Args:
            wid (int): ID of the warehouse to be deleted. 
            data (object): JSON object containing information of the warehouse to be updated.

        Returns:
            ID of the user that was updated in JSON format.
        """
        warehouse_name = data['wname']
        warehouse_country = data['wcountry']
        warehouse_region = data['wregion']
        warehouse_city = data['wcity']
        warehouse_street = data['wstreet']
        warehouse_zipcode = data['wzipcode']
        warehouse_budget = data['wbudget']
        
        if len(data) != 7:
            return jsonify(Error='Malformed update request'), 400
        
        elif warehouse_name and warehouse_country and warehouse_region and warehouse_city \
        and warehouse_street and warehouse_zipcode and (warehouse_budget and warehouse_budget >= 0):
            
            flag = self.warehouseDAO.updateWarehouseByID(wid,warehouse_name,warehouse_country,warehouse_region,warehouse_city,
                                                    warehouse_street,warehouse_zipcode,warehouse_budget)
            if flag:
                return jsonify(data), 200
            else:
                return jsonify(Error='Warehouse Not Found'), 404
        else:
            return jsonify(Error='Unexpected attribute values'), 400
        
    def deleteWarehouseByID(self,wid:int) -> object:
        """Delete a warehouse from the Warehouses Table in the database by the given ID.

        Args:
            wid (int): ID of the warehouse to be deleted.

        Returns:
            ID of the warehouse that was deleted in JSON format.
        """
        if not wid:
            return jsonify(Error='Malformed delete request'), 400
        elif not self.warehouseDAO.getWarehouseByID(wid):
            return jsonify(Error='Warehouse Not Found'), 404
        else:
            wid = self.warehouseDAO.deleteWarehouseByID(wid)
            return jsonify(wid), 200
        