import psycopg2
from dataBaseConnector import dataBaseConnector

class toDoAppConnector(dataBaseConnector):

    def listAll(self):
        list_sql = "select * from todo;"
        self.cursor.execute(list_sql)
        records = self.cursor.fetchall()
        for record in records:
            print(record[0], end="")
            print(' - ', end="")
            print(record[1])

    def insert(self, thing=""):

        try:
            #finout the max id in doto table
            find_max_sql = "select max(id) from todo;"
            self.cursor.execute(find_max_sql)
            max_id = int(self.cursor.fetchall())

            #insert thing with max_id
            insert_sql = "insert into todo (id, thing) values (%s, %s)"
            record_to_insert = (max_id + 1, thing)
            self.cursor.execute(insert_sql, record_to_insert)
            self.connection.commit()

        except (Exception, psycopg2.Error) as error:
            if(self.connection):
                print("Failed to insert record into todo table", error)

    #check the task if it has been done
    #no returns
    #print out the result
    def check_by_id(self, id):
        pass