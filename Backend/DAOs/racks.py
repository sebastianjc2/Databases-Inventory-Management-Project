from Backend.DAOs.DAO import DAO


class RackDAO(DAO):
    def getAllRacks(self):
        cur = self.conn.cursor()
        res = []
        query = "select rid, rname, rcapacity from racks"
        cur.execute(query)

        for row in cur:
            res.append(row)
        return res

    def addRack(self, rname, rcapacity):
        cur = self.conn.cursor()
        query = "INSERT INTO racks(rname, rcapacity) VALUES (%s, %s) returning rid;"
        cur.execute(query, (rname, rcapacity))
        rid = cur.fetchone()[0]
        self.conn.commit()
        return rid

    def getRackById(self, rid):
        cursor = self.conn.cursor()
        query = "select rid, rname, rcapacity from racks where rid = %s;"
        cursor.execute(query, (rid,))

        res = cursor.fetchone()
        print("res:", res)
        return res

    def modifyRackById(self, rid, rname, rcapacity):
        cursor = self.conn.cursor()
        query = "UPDATE racks SET rname = %s, rcapacity = %s WHERE rid = %s;"
        cursor.execute(query, (rname, rcapacity, rid))
        count = cursor.rowcount
        print(count)
        self.conn.commit()
        return count

    def deleteRackById(self, rid):
        cur = self.conn.cursor()
        query = "DELETE FROM racks WHERE rid = %s"
        cur.execute(query, (rid,))
        count = cur.rowcount
        self.conn.commit()
        return count
    
    def get_capacity(self, rid):
        result = self._generic_retrieval_query(query="""
                                               SELECT rcapacity
                                               FROM racks
                                               WHERE rid = %s
                                               """,
                                               substitutions=rid)
        if not result: return None
        return result[0][0]