from flask import jsonify
from Backend.DAOs.user_dao import UserDAO
from Backend.DAOs.warehouse_dao import WarehouseDAO

class UserHandler:
    """
    UserHandler takes care of processing all the data
    from the user and transforming it into a JSON
    to be sent to the database in order to be processed.
    The handler also takes care of connecting to the DB
    and extract lists of users.
    """
    
    def __init__(self):
        # Capture in an object the query to be sent to the DB.
        self.userDAO = UserDAO()
        self.warehouseDAO = WarehouseDAO()
        self.user_cols = ['uid','ufname','ulname','username','uemail','upassword','wid']
    
    def build_user_dict(self,row:tuple) -> dict:
        """Builds dictionary that contains
        all the information from a user.

        Args:
            row (tuple): A record, given as a tuple, from the
        Users table in the database.

        Returns:
            dict: A dictionary that contains all the information mapped to
        the correct keys. This is so that later the dictionary can be 
        transformed into JSON format.
        """
        user_dict = {}
#       keys = ['uid','ufname','ulname','username','uemail','upassword','wid']
#        for index,key in enumerate(keys):
#            user_dict[key] = row[index]


        user_dict['uid'] = row[0]
        user_dict['ufname'] = row[1]
        user_dict['ulname'] = row[2]
        user_dict['username'] = row[3]
        user_dict['uemail'] = row[4]
        user_dict['upassword'] = row[5]
        user_dict['wid'] = row[6]
        
        return user_dict
        
    
    def getAllUsers(self) -> object:
        """Returns all users from the Users Table in the database.
    
        Return: JSON object that contains all the users from the Users Table that were found in the database.
        """
        
        all_users_tuples = self.userDAO.getAllUsers()
        all_users_result = []
        for record in all_users_tuples:
            all_users_result.append(self.build_user_dict(record))
        return jsonify(Users=all_users_result)
    
    def getUserByID(self,uid:int) -> object:
        """ Return a record, or series of records that correspond to the user with the given uid.

        Args:
            uid (int): The uid of the user to be searched.

        Returns:
            object: JSON object that contains all the data found of the user with the given uid.
        """
        
        uid_row = self.userDAO.getUserByID(uid)
        # If the user was not found, return a 404 error.
        if not uid_row:
            return jsonify(Error="User Not Found"),404
        return jsonify(User=self.build_user_dict(uid_row[0]))
    
    def insertUser(self,data:object):
        """Insert a user with the given data in the users table

        Args:
            data (object): JSON object containing information
            to create a user.

        Returns:
            _type_: JSON object that contains the ID of the user that was inserted.
        """
        if data:
            ufname = data['ufname']
            ulname = data['ulname']
            username = data['username']
            uemail = data['uemail']
            upassword = data['upassword']
            wid = data['wid']
            
            if not self.warehouseDAO.getWarehouseByID(wid):
                return jsonify(Error="User can not belong to a Warehouses that does not exist"),404
            
            elif ufname and ulname and username and uemail and upassword and wid:
                uid = self.userDAO.insertUser(ufname,ulname,username,uemail,upassword,wid)
                # TODO: Refactor this so it is not hardcoded.
                inserted_user = {}
                inserted_user['uid'] = uid
                inserted_user['ufname'] = ufname
                inserted_user['ulname'] = ulname
                inserted_user['username'] = username
                inserted_user['uemail'] = uemail
                inserted_user['upassword'] = upassword
                inserted_user['wid'] = wid
                return jsonify(User=inserted_user),201
            else:
                return jsonify(Error="Unexpected attributes in post request"),400
        return jsonify(Error="Malformed post request"),400
            
    def updateUserByID(self,uid:int,data:object) -> object:
        if not data:
            return jsonify(Error="Malformed update request"),400
        elif not self.userDAO.getUserByID(uid):
            return jsonify(Error="User not found"),404
        elif len(data) != 6:
            return jsonify(Error="Malformed update request"),400
        else:
            wid = data['wid']
            if not self.warehouseDAO.getWarehouseByID(wid):
                return jsonify(Error="User can not belong to a Warehouses that does not exist"),404
            ufname = data['ufname']
            ulname = data['ulname']
            username = data['username']
            uemail = data['uemail']
            upassword = data['upassword']
            if ufname and ulname and username and uemail and upassword and wid:
                updated_user = self.userDAO.updateUserByID(uid,ufname,ulname,username,uemail,upassword,wid)
                return jsonify("Updated user with id: {}, ".format(updated_user)),200
            else:
                return jsonify(Error="Unexpected attributes in update request"),400
            
    def deleteUserByID(self,uid:int) -> object:
        """Delete a user from the Users table with the given uid.

        Args:
            uid (int): ID of the user to be deleted.

        Returns:
            object: JSON object that contains the ID of the deleted user.
        """
        if not uid:
            return jsonify(Error="Malformed delete request"),400
        
        elif not self.userDAO.getUserByID(uid):
            return jsonify(Error="User not found"),404
        else:
            deleted_user_id = self.userDAO.deleteUserByID(uid)
            return jsonify('Deleted user with id: {}'.format(deleted_user_id)),200


    def getTopTransactions(self):
        """Part of the Global Statistics.Top 3 users that made the most transactions."""
        transaction_results = self.userDAO.get_most_transactions()
        if not transaction_results:
            return jsonify(Error='No Results were returned.'), 404
        else:
            return jsonify(transaction_results), 200
            
            
            
        
    
            
        
        
        
    
