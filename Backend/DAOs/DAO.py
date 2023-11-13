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
