from typing import Iterable
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


    def _getAllEntries(self, table_name: str, columns: tuple) -> Iterable | None:
        """
        Selects the given attributes from the given table.
        Returns the list of tuples returned from the query or None if the operation failed.
        """
        cursor = self.conn.cursor()
        query = f"SELECT {', '.join(columns)} FROM {table_name}"
        return self._generic_retrieval_query(query)
    

    def _getEntryByID(self, table_name: str, id_name: str, id_value: str, columns: tuple) -> Iterable | None:
        """
        Selects the given attributes that match the given id.
        Returns the matching entries or None if the operation failed.
        """
        cursor = self.conn.cursor()
        query = f"""
        SELECT {', '.join(columns)}
        FROM {table_name}
        WHERE {id_name} = %s
        """
        return self._generic_retrieval_query(query, substitutions=(id_value,))
    

    def _addEntry(self, table_name: str, id_name: str, columns: list, values: list) -> int | None:
        """
        Inserts a tuple with the given attributes.
        Returns the auto-generated id or None if the operation failed.
        """
        cursor = self.conn.cursor()
        query = f"""
        INSERT INTO {table_name}({', '.join(columns)})
        VALUES ({('%s,'*len(values)).rstrip(',')})
        RETURNING {id_name};
        """
        try:
            cursor.execute(query, values)
            entry_id = cursor.fetchone()[0]
            self.conn.commit()
            return entry_id
        except psycopg2.errors.Error as e:
            print(e.pgerror)
            return None
    

    def _modifyEntryByID(self, table_name: str, id_name: str, id_value: str, columns: list, values: list) -> int | None:
        """
        Modifies the tuple with the given id.
        Returns the number of rows affected by the operation or None if the operation failed.
        """
        cursor = self.conn.cursor()
        set_statement = "SET"
        for column in columns:
            set_statement += f" {column} = %s,"
        query = f"UPDATE {table_name} {set_statement.rstrip(',')} WHERE {id_name} = %s;"
        try:
            cursor.execute(query, (*values, id_value))
            count = cursor.rowcount
            self.conn.commit()
            return count
        except psycopg2.errors.Error as e:
            print(e.pgerror)
            return None
    

    def _deleteEntryByID(self, table_name: str, id_name: str, id_value: str) -> int | None:
        """
        Deletes the tuple with the given id.
        Returns the number of rows affected by the operation or None if the operation failed.
        """
        cursor = self.conn.cursor()
        query = f"DELETE FROM {table_name} WHERE {id_name} = %s"
        try:
            cursor.execute(query, (id_value,))
            count = cursor.rowcount
            self.conn.commit()
            return count
        except psycopg2.errors.Error as e:
            print(e.pgerror)
            return None


    def _generic_retrieval_query(self, query: str, substitutions=()) -> Iterable | None:
        """
        Executes the given query and returns the result.
        Useful for custom queries requiring joins or None if the operation failed.
        Returns the tuples matched by the query or None if the operation failed.
        """
        cursor = self.conn.cursor()
        if not isinstance(substitutions, Iterable): substitutions = (substitutions,)
        try:
            cursor.execute(query, substitutions)
            res = []
            for row in cursor:
                print("row:", row)
                res.append(row)
            return res
        except psycopg2.errors.Error as e:
            print(e.pgerror)
            return None
