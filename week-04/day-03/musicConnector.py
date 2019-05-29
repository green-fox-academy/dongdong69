import psycopg2
from dataBaseConnector import dataBaseConnector

class musicConnector(dataBaseConnector):

    def insert(self, name, title):
        insert_sql = "insert into music (id, name, title, state) values (%s, %s, %s, 0)"
        
        #find out the max id in music table
        find_max_sql = "select max(id) from music;"
        self.cursor.execute(find_max_sql)
        max_id = self.cursor.fetchone()[0]

        try:
            record_to_insert = (max_id + 1, name, title)
            self.cursor.execute(insert_sql, record_to_insert)
            #save the changes
            self.connection.commit()
            #count the row been changed
            count = self.cursor.rowcount
            if count:
                print(count, "Record insert successfully")
        except (Exception, psycopg2.Error) as error:
            if(self.connection):
                print("Failed to insert record into music table", error)

    def list_records(self, name="", both=False):
        if not name:
            list_sql = "select * from music;"
            self.cursor.execute(list_sql)
            records = self.cursor.fetchall()
            for record in records:
                print(record)

    def delete(self, id):
        try:
            delete_sql = "delete from music where id=%s"
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
                print(f"Failed to delete No.{id} music", error)

    def play(self, id):

        playing_music_sql = "select * from music where state=1"
        self.cursor.execute(playing_music_sql)
        playing_music = self.cursor.fetchone()

        if playing_music:
            print(f"Sorry!! {playing_music} is playing, you cannot play another one.")
            stop = input("Would you like to stop it?(Y|N)")
            if stop == 'Y':
                update_sql = "Update music set state = 0 where state = 1"
                self.cursor.execute(update_sql)
                self.connection.commit()
                count = self.cursor.rowcount
                if count:
                    print(f"{playing_music} has benn stoped.")
                    print("Now you can play other music.")
            else:
                print(f"{playing_music} is still playing, Enjoy!")

        else:
            update_sql = "Update music set state = 1 where id = %s"
            try:
                self.cursor.execute(update_sql, id)
                #save the changes
                self.connection.commit()
                #count the row been changed
                count = self.cursor.rowcount
                if count:
                    print(count, "Record deleted successfully")
                    print(f"Now music No.{id} is playing, Enjoy!")
                else:
                    print(f"record No.{id} is not in the database.")
                    print("Please try another one.")

            except (Exception, psycopg2.Error) as error:
                if(self.connection):
                    print(f"Failed to play No.{id} music", error)