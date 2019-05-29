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
            max_id = self.cursor.fetchone()[0]

            #insert thing with max_id
            insert_sql = "insert into todo (id, thing) values (%s, %s)"
            record_to_insert = (max_id + 1, thing)
            self.cursor.execute(insert_sql, record_to_insert)
            #save the changes
            self.connection.commit()
            #count the row been changed
            count = self.cursor.rowcount
            if count:
                print(count, "Record insert successfully")

        except (Exception, psycopg2.Error) as error:
            if(self.connection):
                print("Failed to insert record into todo table", error)

    #check the task if it has been done
    #no returns
    #print out the result
    def check_by_id(self, id):
        try:
            check_sql = "select * from todo where id=%s"
            self.cursor.execute(check_sql, id)
            result = self.cursor.fetchall()
            if result:
                print(f"{result[0]} havent been done yet.")
            else:
                print("It is already been done.")
        
        except (Exception, psycopg2.Error) as error:
            if(self.connection):
                print("Failed to find the record in todo table", error)

    #remove the record in the database by id
    def remove(self, id):
        try:
            delete_sql = "delete from todo where id=%s"
            self.cursor.execute(delete_sql, id)
            #save the changes
            self.connection.commit()
            #count the row been changed
            count = self.cursor.rowcount
            if count:
                print(count, "Record deleted successfully")
            else:
                print(f"record No.{id} is not in the database")

        except (Exception, psycopg2.Error) as error:
            if(self.connection):
                print(f"Failed to delete No.{id} task from todo", error)