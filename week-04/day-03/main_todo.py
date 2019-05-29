import sys
import getopt
from toDoAppConnector import toDoAppConnector

def main(argv):
    #init a connector
    connector = toDoAppConnector("task")
    try:
        opts, args = getopt.getopt(argv, "la:c:r:")
    except getopt.GetoptError:
        print("error: -l list everything in the database")
        print("   or: -a <task> add a new task")
        print("   or: -c <id> check the task if it has been done")
        print("   or: -r <id> remove a task")

    for opt, arg in opts:
        #do list
        if opt == "-l":
            connector.listAll()
        #add record
        elif opt == "-a":
            connector.insert(arg)
        #check record
        elif opt == "-c":
            connector.check_by_id(arg)
        #remove record in the database
        elif opt == "-r":
            connector.remove(arg)

    #close the database
    connector.close_database()

#run this
if __name__ == "__main__":
    main(sys.argv[1:])