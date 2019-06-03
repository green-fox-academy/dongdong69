from dataBaseConnector import dataBaseConnector

class slackConnector(dataBaseConnector):

    def insert_users(self, user_set):
        insert_sql = "insert into users (user_id, name) values (%s, %s);"
        for index, Uid in enumerate(user_set):
            Uid_index = (str(index), Uid)
            self.cursor.execute(insert_sql, Uid_index)
            self.connection.commit()

    def find_user_id(self, name):
        search_sql = "select user_id from users where name=%s;"
        self.cursor.execute(search_sql, (name,))
        user_id = self.cursor.fetchone()[0]
        return user_id

    def insert_messages(self, records):
        insert_sql = "insert into messages (message_id, user_id, message, channel, sent_at) values (%s, %s, %s, %s, %s);"
        for record in records:
            insert_record = (record["message_id"], record["user_id"], record["message"], record["channel"], record["sent_at"])
            self.cursor.execute(insert_sql, insert_record)
            self.connection.commit()

    def insert_reactions(self, records):
        insert_sql = "insert into reactions (id, user_id, message_id, reaction) values (%s, %s, %s, %s);"
        for index, record in enumerate(records):
            insert_record = (index, record["user_id"], record["message_id"], record["reaction"])
            self.cursor.execute(insert_sql, insert_record)
            self.connection.commit()


    def insert_mentions(self, records):
        insert_sql = "insert into mentions (message_id, user_id) values (%s, %s);"
        for record in records:
            insert_record = (record["message_id"], record["user_id"])
            self.cursor.execute(insert_sql, insert_record)
            self.connection.commit()

    def insert_replies(self, records):
        insert_sql = "insert into replies (message_id, user_id) values (%s, %s);"
        for record in records:
            insert_record = (record["message_id"], record["reply_id"])
            self.cursor.execute(insert_sql, insert_record)
            self.connection.commit()

    def search_by_name(self, name):
        pass

    def search_by_time(self, start_time, end_time):
        pass

    def select_user_helper(self):
        search_sql = "select messages.user_id as usser_id, mentions.user_id as helper_id from mentions left join messages on mentions.message_id = messages.message_id;"
        self.cursor.execute(search_sql)
        results = self.cursor.fetchall()
        return results

    def select_parent_child(self):
        search_sql = "select messages.user_id as parent_id, replies.user_id as child_id from replies left join messages on replies.message_id = messages.message_id;"
        self.cursor.execute(search_sql)
        results = self.cursor.fetchall()
        return results