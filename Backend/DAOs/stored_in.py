from Backend.DAOs.DAO import DAO
import psycopg2

class StoredInDAO(DAO):
    def get_quantity(self, wid, pid, rid):
        """
        Returns the quantity of parts currently stored in the rack,
        or 0 if the relationship does not exist.
        """
        result = self._generic_retrieval_query(query="""
                                               SELECT parts_qty
                                               FROM stored_in
                                               WHERE wid = %s
                                               AND pid = %s
                                               AND rid = %s;
                                               """,
                                               substitutions=(wid, pid, rid))
        if not result: return 0
        return result[0][0]

    def modify_quantity_or_insert(self, wid, pid, rid, quantity):
        """
        Sets the quantity to the given value.
        Returns the new number of affected rows.
        """
        cursor = self.conn.cursor()
        if self.get_quantity(wid, pid, rid):
            query = """
            UPDATE stored_in
            SET parts_qty = %s
            WHERE wid = %s
            AND pid = %s
            AND rid = %s;
            """
            values = (quantity, wid, pid, rid)
        else:
            query = """
            INSERT INTO stored_in (wid, pid, rid, parts_qty)
            VALUES (%s, %s, %s, %s)
            """
            values = (wid, pid, rid, quantity)
        try:
            cursor.execute(query, values  )
            count = cursor.rowcount
            self.conn.commit()
            return count
        except psycopg2.errors.Error as e:
            print(f"\n\nError in file: {__file__}\n{e.pgerror}\n\n")
            return None

    def isPartInWarehouse(self, pid, wid):
        result = self._generic_retrieval_query(query="""
                                                       SELECT COUNT(pid)
                                                       FROM stored_in
                                                       WHERE pid = %s
                                                       AND wid = %s;
                                                       """,
                                               substitutions=(pid, wid))
        if not result or len(result) == 0: return 0
        return result[0][0]

    def get_qty_with_rid(self, rid):
        res = self._generic_retrieval_query(query="""
                                            SELECT parts_qty
                                            FROM stored_in
                                            WHERE rid = %s;
                                            """,
                                            substitutions=rid)
        if not res: return 0
        return res[0][0]

