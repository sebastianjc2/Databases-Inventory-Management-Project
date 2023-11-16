from Backend.DAOs.DAO import DAO


class SupplierDAO(DAO):
    def getAllSuppliers(self):
        cur = self.conn.cursor()
        res = []
        query = "select sid, sname, scountry, scity, sstreet, szipcode, sphone from supplier"
        cur.execute(query)

        for row in cur:
            res.append(row)
        return res

    def insertSupplier(self, name, country, city, street, zipcode, phone):
        cur = self.conn.cursor()
        query = "INSERT INTO supplier(sname, scountry, scity, sstreet, szipcode, sphone) VALUES (%s, %s, %s, %s, %s, " \
                "%s) returning sid; "
        cur.execute(query, (name, country, city, street, zipcode, phone))
        sid = cur.fetchone()[0]
        self.conn.commit()
        return sid

    def searchByID(self, sid):
        cur = self.conn.cursor()
        query = "SELECT sid, sname, scountry, scity, sstreet, szipcode, sphone FROM supplier WHERE sid = %s;"
        cur.execute(query, (sid,))
        res = cur.fetchone()
        return res

    def deleteByID(self, sid):
        cur = self.conn.cursor()
        query = "DELETE FROM supplier WHERE sid = %s"
        cur.execute(query,(sid,))
        count = cur.rowcount
        self.conn.commit()
        return count

    def updateByID(self, sid, name, country, city, street, zipcode, phone):
        cur = self.conn.cursor()
        query = "UPDATE supplier SET sname = %s, scountry = %s, scity = %s, sstreet = %s, szipcode = %s, sphone = %s " \
                "WHERE sid = %s; "
        cur.execute(query, (name, country, city, street, zipcode, phone, sid,))
        count = cur.rowcount
        self.conn.commit()
        return count
