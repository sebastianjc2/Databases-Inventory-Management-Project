from Backend.config.dbconfig import pg_config
import psycopg2


class SupplierDAO:
    def __init__(self):
        connection_url = f'host = localhost dbname={(pg_config["dbname"])} user={pg_config["user"]} password={pg_config["password"]}'

        print("Connection url:", connection_url)
        self.conn = psycopg2.connect(connection_url)  # connection URL to the DB to send queries

    def getAllSuppliers(self):
        cur = self.conn.cursor()
        res = []
        query = "select sid, sfname, slname, scountry, scity, sstreet, szipcode, sphone from supplier"
        cur.execute(query)

        for row in cur:
            res.append(row)
        return res

    def insertSupplier(self, fname, lname, country, city, street, zipcode, phone):
        cur = self.conn.cursor()
        query = "INSERT INTO supplier(sfname, slname, scountry, scity, sstreet, szipcode, sphone) VALUES (%s, %s, %s, %s, %s, %s, %s) returning sid;"
        cur.execute(query, (fname, lname, country, city, street, zipcode, phone))
        sid = cur.fetchone()[0]
        self.conn.commit()
        return sid
