from Backend.DAOs.DAO import DAO

class CustomerDAO(DAO):
    def getAllCustomers(self):
        cursor = self.conn.cursor()
        res = []
        query = "select cid, cfname, clname, czipcode, cphone from customer"
        cursor.execute(query)

        for row in cursor:
            print("row:", row)
            res.append(row)
        return res
    
    def addCustomer(self, cfname, clname, czipcode, cphone):
        cursor = self.conn.cursor()
        query = "INSERT INTO customer(cfname, clname, czipcode, cphone) VALUES (%s, %s, %s, %s) returning cid;"
        cursor.execute(query, (cfname, clname, czipcode, cphone))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid
    
    def getCustomerById(self, cid):
        cursor = self.conn.cursor()
        res = []
        query = """
        select cid, cfname, clname, czipcode, cphone
        from customer
        where cid = %s
        """
        cursor.execute(query, (str(cid)))

        for row in cursor:
            print("row:", row)
            res.append(row)
        return res
    

    def modifyCustomerById(self, cfname, clname, czipcode, cphone, cid):
        cursor = self.conn.cursor()
        query = """
        UPDATE customer
        SET cfname = %s, clname = %s, czipcode = %s, cphone = %s
        WHERE cid = %s;
        """
        cursor.execute(query, (cfname, clname, czipcode, cphone, cid))
        count = cursor.rowcount
        self.conn.commit()
        return count
    

    def deleteCustomerById(self, cid):
        cur = self.conn.cursor()
        query = "DELETE FROM customer WHERE cid = %s"
        cur.execute(query, (cid))
        count = cur.rowcount
        self.conn.commit()
        return count