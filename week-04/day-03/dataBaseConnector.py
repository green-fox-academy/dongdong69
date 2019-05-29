import psycopg2

class dataBaseConnector:

    #init database
    def __init__(self, database_name):
        self.connection = psycopg2.connect(
            user="postgres",
            password="ccd9775301",
            host="127.0.0.1",
            port="5432",
            database=database_name
        )

        self.cursor = self.connection.cursor()

    #close the connected database
    def close_database(self):
        if(self.connection):
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")
        else:
            print("Failed to close the connection")