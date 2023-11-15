from Backend.dbconfig import pg_config
import psycopg2

class DAO:
    """
    Base class for all DAOs.
    Initializes the connection.
    """
    def __init__(self):
        connection_url = (
            f'host = localhost dbname={(pg_config["dbname"])} '
            f'user={pg_config["user"]} password={pg_config["password"]}'
        )
        print("Connection url:", connection_url)
        self.conn = psycopg2.connect(connection_url)


    """
    The following are 'internal' functions to perform some of the more common operations.
    """


    def _getAllEntries(self, table_name: str, columns: tuple):
        """
        Selects the given attributes from the given table.
        Returns the list of tuples returned from the query
        """
        cursor = self.conn.cursor()
        query = f"SELECT {', '.join(columns)} FROM {table_name}"
        cursor.execute(query)
        res = []
        for row in cursor:
            print("row:", row)
            res.append(row)
        return res
    

    def _getEntryByID(self, table_name: str, id_name: str, id_value: str, columns: tuple):
        """
        Selects the given attributes that match the given id.
        Returns the matchin entries.
        """
        cursor = self.conn.cursor()
        query = f"""
        SELECT {', '.join(columns)}
        FROM {table_name}
        WHERE {id_name} = %s
        """
        cursor.execute(query, (id_value))
        res = []
        for row in cursor:
            print("row:", row)
            res.append(row)
        return res
    

    def _addEntry(self, table_name: str, id_name: str, columns: list, values: list):
        """
        Inserts a tuple with the given attributes.
        Returns the auto-generated id.
        """
        cursor = self.conn.cursor()
        query = f"""
        INSERT INTO {table_name}({', '.join(columns)})
        VALUES ({('%s,'*len(values)).rstrip(',')})
        RETURNING {id_name};
        """
        cursor.execute(query, values)
        entry_id = cursor.fetchone()[0]
        self.conn.commit()
        return entry_id
    

    def _modifyEntryByID(self, table_name: str, id_name: str, id_value: str, columns: list, values: list):
        """
        Modifies the tuple with the given id.
        Returns the number of rows affected by the operation.
        """
        cursor = self.conn.cursor()
        set_statement = "SET"
        for column in columns:
            set_statement += f" {column} = %s,"
        query = f"UPDATE {table_name} {set_statement.rstrip(',')} WHERE {id_name} = %s;"
        cursor.execute(query, (*values, id_value))
        count = cursor.rowcount
        self.conn.commit()
        return count
    

    def _deleteEntryByID(self, table_name: str, id_name: str, id_value: str):
        """
        Deletes the tuple with the given id.
        Returns the number of rows affected by the operation.
        """
        cursor = self.conn.cursor()
        query = f"DELETE FROM {table_name} WHERE {id_name} = %s"
        cursor.execute(query, (id_value))
        count = cursor.rowcount
        self.conn.commit()
        return count


    def _generic_query(self, query: str, substitutions=()):
        """
        Executes the given query and returns the result.
        Useful for custom queries requiring joins.
        """
        cursor = self.conn.cursor()
        cursor.execute(query, substitutions)
        res = []
        for row in cursor:
            print("row:", row)
            res.append(row)
        return res