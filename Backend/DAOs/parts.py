from Backend.dbconfig import pg_config
import psycopg2

class PartDAO:
    def __init__(self):
        # host = localhost is important!. If it's in heroku it would change. Also, the port could be important too!
        connection_url = (f'host = localhost dbname={(pg_config["dbname"])} '
                          f'user={pg_config["user"]} password={pg_config["password"]}')

        print("Connection url:", connection_url)
        self.conn = psycopg2.connect(connection_url) # connection URL to the DB to send queries

    def getAllParts(self):
        # object utilized to send queries to the DB and too iterate through the results from the query
        cursor = self.conn.cursor()
        res = []
        query = "select pid, pname, pcolor, pmaterial, msrp from parts"
        cursor.execute(query)

        for row in cursor:
            print("row:", row)
            res.append(row)  # adding the rows
        return res

    def searchByID(self, pid):
        cursor = self.conn.cursor()
        query = "SELECT pid, pname, pcolor, pmaterial, msrp FROM parts WHERE pid = %s"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result

    def insertPart(self, name, color, material, msrp):
        cursor = self.conn.cursor()
        query = "INSERT INTO parts(pname, pcolor, pmaterial, msrp) VALUES (%s, %s, %s, %s) returning pid;"
        cursor.execute(query, (name, color, material, msrp))  # passing the args so it's more secure
        pid = cursor.fetchone()[0]
        self.conn.commit()  # to save the changes
        return pid

    def deleteByID(self, pid):
        cursor = self.conn.cursor()
        query = "DELETE FROM parts WHERE pid = %s"
        cursor.execute(query, (pid,))
        count = cursor.rowcount
        self.conn.commit()  # to save the changes
        return count

    def updateByID(self, pid, name, color, material, msrp):
        cursor = self.conn.cursor()
        query = "UPDATE parts set pname=%s, pcolor=%s, pmaterial=%s, msrp=%s where pid = %s;"
        cursor.execute(query, (name, color, material, msrp, pid,))  # passing the args so it's more secure
        count = cursor.rowcount
        self.conn.commit()  # to save the changes
        return count
