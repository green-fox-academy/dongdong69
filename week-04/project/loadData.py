from slackConnector import slackConnector
from jsonReader import jsonReader
import time
import re

def main():
    #read the thanks file
    jsonr = jsonReader('week-04\project\gfa-team-thanks.json')
    records = jsonr.get_records()
    string_records = jsonr.get_string()

    #read the file with replies
    jsonr = jsonReader('week-04\project\gfa-team-thanks-replies.json')
    records_reply = jsonr.get_records()
    string_records_reply = jsonr.get_string()

    Uid_list = catch_Uid(string_records)
    Uid_list_reply = catch_Uid(string_records_reply)

    #save all user_name in a set
    user_set = set()
    for Uid in Uid_list:
        user_set.add(Uid)

    for Uid in Uid_list_reply:
        user_set.add(Uid)

    #connect the database
    connector = slackConnector('Slack analysis')
    #store the information into users table
    #connector.insert_users(user_set)

    records_list = []
    reactions_list = []

    #insert the result into table messages
    for record in records:

        record_dict = {
            "message_id" : "",
            "user_id" : "",
            "message" : "",
            "channel" : "thanks",
            "sent_at" : ""
        }

        if "client_msg_id" in record:
            record_dict["message_id"] = record["client_msg_id"]
            record_dict["user_id"] = connector.find_user_id(record["user"])
            record_dict["message"] = record["text"]

            timeStamp = float(record["ts"])
            timeArray = time.localtime(timeStamp)
            record_dict["sent_at"] = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

            records_list.append(record_dict)

        if "reactions" in record and "client_msg_id" in record:
            message_id = record["client_msg_id"]
            for reaction in record["reactions"]:
                reaction_name = reaction["name"]
                for user in reaction["users"]:
                    reaction_dict = {
                        "user_id" : "",
                        "message_id" : "",
                        "reaction" : ""
                    }
                    reaction_dict["user_id"] = connector.find_user_id(user)
                    reaction_dict["reaction"] = reaction_name
                    reaction_dict["message_id"] = message_id
                    reactions_list.append(reaction_dict)

    mentions_list = []


    for record in records:

        if "text" in record and "client_msg_id" in record:
            message_id = record["client_msg_id"]
            text = record["text"]
            uids = catch_Uid(text)
            if not uids:
                continue
            else:
                for uid in uids:
                    mention_dict = {
                        "message_id" : "",
                        "user_id" : ""
                    }
                    mention_dict["message_id"] = message_id
                    mention_dict["user_id"] = connector.find_user_id(uid)
                    mentions_list.append(mention_dict)

    #insert into messages
    #connector.insert_messages(records_list)

    #insert into reactions
    #connector.insert_reactions(reactions_list)

    #insert into mentions
    #connector.insert_mentions(mentions_list)

    replies_list = []

    for record in records:

        if "client_msg_id" in record and "reply_users" in record:
             message_id = record["client_msg_id"]

             for replayer in record["reply_users"]:
                reply_dict = {
                    "message_id" : "",
                    "reply_id" : ""
                }
                reply_dict["message_id"] = message_id
                reply_dict["reply_id"] = connector.find_user_id(replayer)
                replies_list.append(reply_dict)

    #insert result into replies table
    #connector.insert_replies(replies_list)

    records_list = []
    comments_list = []

    #insert the result into table messages
    
    for record in records_reply:

        record_dict = {
            "message_id" : "",
            "user_id" : "",
            "message" : "",
            "channel" : "thanks",
            "sent_at" : ""
        }

        if "parent_user_id" in record and "client_msg_id" in record:
            print("in")
            record_dict["message_id"] = record["client_msg_id"]
            record_dict["user_id"] = connector.find_user_id(record["user"])
            record_dict["message"] = record["text"]

            timeStamp = float(record["ts"])
            timeArray = time.localtime(timeStamp)
            record_dict["sent_at"] = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            records_list.append(record_dict)

    connector.insert_messages(records_list)

    #close the database
    connector.close_database()

#catch the id in the string
def catch_Uid(string):
    Uid_list = re.findall("U[A-Z0-9]{8}", string)
    return Uid_list

#run this
if __name__ == "__main__":
    main()