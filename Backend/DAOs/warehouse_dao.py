from Backend.DAOs.DAO import DAO
import psycopg2


class WarehouseDAO(DAO):

    def getAllWarehouses(self):
        """Execute a query to get all the warehouses from the Warehouses Table in the database.
        
        Return: all records from the Warehouses Table in the database.
        """
        return self._getAllEntries(table_name="warehouse",
                                   columns=("wid",
                                            "wname",
                                            "wcountry",
                                            "wregion",
                                            "wcity",
                                            "wstreet",
                                            "wzipcode",
                                            "wbudget"))

    def insertWarehouse(self, warehouse_name: str,
                        warehouse_country: str,
                        warehouse_region: str,
                        warehouse_city: str,
                        warehouse_street: str,
                        warehouse_zipcode: str,
                        warehouse_budget: float) -> int:
        """Insert a new warehouse in the Warehouses Table in the database.

        Args:
            warehouse_name (str): Name of the warehouse to be inserted.
            warehouse_country (str): Country of the warehouse to be inserted.
            warehouse_region (str): Region of the warehouse to be inserted.
            warehouse_city (str): City of the warehouse to be inserted.
            warehouse_street (str): Street of the warehouse to be inserted.
            warehouse_zipcode (str): Zipcode of the warehouse to be inserted.
            warehouse_budge (float): Budget of the warehouse to be inserted.

        Returns:
            int: ID of the warehouse that was inserted.
        """
        return self._addEntry(table_name="warehouse",
                              id_name="wid",
                              columns=["wname", "wcountry", "wregion", "wcity", "wstreet", "wzipcode", "wbudget"],
                              values=[warehouse_name,
                                      warehouse_country,
                                      warehouse_region,
                                      warehouse_city,
                                      warehouse_street,
                                      warehouse_zipcode,
                                      warehouse_budget])

    def getWarehouseByID(self, wid: int):
        """Execute a query to get a warehouse from the Warehouses Table in the database.
        
        Return: a record from the Warehouses Table in the database which matches the given wid.
        """
        return self._getEntryByID(table_name="warehouse", id_name="wid", id_value=str(wid),
                                  columns=("wid", "wname", "wcountry", "wregion", "wcity", "wstreet", "wzipcode",
                                           "wbudget"))

    def insertWarehouse(self, warehouse_name: str,
                        warehouse_country: str,
                        warehouse_region: str,
                        warehouse_city: str,
                        warehouse_street: str, warehouse_zipcode: str,
                        warehouse_budget: float) -> int:
        """Insert a new warehouse in the Warehouses Table in the database.

        Args:
            warehouse_name (str): Name of the warehouse to be inserted.
            warehouse_country (str): Country of the warehouse to be inserted.
            warehouse_region (str): Region of the warehouse to be inserted.
            warehouse_city (str): City of the warehouse to be inserted.
            warehouse_street (str): Street of the warehouse to be inserted.
            warehouse_zipcode (str): Zipcode of the warehouse to be inserted.
            warehouse_budge (float): Budget of the warehouse to be inserted.

        Returns:
            int: ID of the warehouse that was inserted.
        """
        return self._addEntry(table_name="warehouse",
                              id_name="wid",
                              columns=["wname", "wcountry", "wregion", "wcity", "wstreet", "wzipcode", "wbudget"],
                              values=[warehouse_name,
                                      warehouse_country,
                                      warehouse_region,
                                      warehouse_city,
                                      warehouse_street,
                                      warehouse_zipcode,
                                      warehouse_budget])

    def updateWarehouseByID(self, wid: int, warehouse_name: str,
                            warehouse_country: str,
                            warehouse_region: str,
                            warehouse_city: str,
                            warehouse_street: str, warehouse_zipcode: str,
                            warehouse_budget: float) -> object:
        return self._modifyEntryByID(table_name="warehouse",
                                     id_name="wid",
                                     id_value=str(wid),
                                     columns=["wname",
                                              "wcountry",
                                              "wregion",
                                              "wcity",
                                              "wstreet", "wzipcode", "wbudget"],
                                     values=[warehouse_name,
                                             warehouse_country,
                                             warehouse_region,
                                             warehouse_city,
                                             warehouse_street,
                                             warehouse_zipcode,
                                             warehouse_budget])

    def deleteWarehouseByID(self, wid: int) -> object:
        """Delete a warehouse from the Warehouses Table in the database by the given ID.

        Args:
            wid (int): ID of the warehouse to be deleted.

        Returns:
            object: ID of the warehouse that was deleted.
        """
        return self._deleteEntryByID(table_name="warehouse",
                                     id_name="wid",
                                     id_value=str(wid))

    def get_warehouse_budget(self, wid):
        result = self._generic_retrieval_query(query="""
                                               SELECT wbudget
                                               FROM warehouse
                                               WHERE wid = %s
                                               """,
                                               substitutions=wid)
        if not result or len(result) == 0: return None
        return result[0][0]

    def decrease_budget(self, wid, delta):
        """
        Decreases the budget by the given delta.
        Returns the new number of affected rows.

        WARNING: If delta is negative or 0, will return None and not execute any operations.
        """
        if delta <= 0: return None
        cursor = self.conn.cursor()
        query = "UPDATE warehouse SET wbudget = wbudget-%s WHERE wid = %s AND wbudget >= %s"
        try:
            cursor.execute(query, (delta, wid, delta))
            count = cursor.rowcount
            self.conn.commit()
            return count
        except psycopg2.errors.Error as e:
            print(f"\n\nError in file: {__file__}\n{e.pgerror}\n\n")
            return None

    def get_top_racks(self):
        """Part of the Global Statistics. Gets the top 10 warehouses with the most racks."""
        query = """SELECT wname as warehouse, COUNT(rid) as rack_count
                    FROM warehouse NATURAL INNER JOIN stored_in
                    GROUP BY wname
                    ORDER BY rack_count DESC
                    LIMIT 10;"""
        return self._generic_retrieval_query(query)

    def get_most_exchanges(self):
        """Part of the Global Statistics. Gets the top 5 warehouses
        with the most exchanges/transfers."""
        query = """SELECT wname as warehouse, COUNT(*) as total_transfers
                    FROM warehouse
                    NATURAL INNER JOIN transactions
                    NATURAL INNER JOIN transfer
                    GROUP BY wname
                    ORDER BY total_transfers DESC
                    LIMIT 5;"""
        return self._generic_retrieval_query(query)
