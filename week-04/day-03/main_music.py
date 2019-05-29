import sys
from musicConnector import musicConnector

def main(argv):

    connection = musicConnector("music")

    args = sys.argv

    if args[1] == 'l':
        try:
            if args[2] == '--artist':
                artist = args[3]
                print(artist)
            else:
                title_or_name = args[2]
                print(title_or_name)
        except:
            connection.list_records()

    elif args[1] == 'a':
        try:
            if args[2] == '--artist':
                try:
                    artist = args[3]
                    title = args[5]
                    connection.insert(artist, title)
                except:
                    print("invild input(ex. a --artist <name> --title <title>)")
            elif args[2]:
                title_and_artist = args[2:]
                string = ""
                for item in title_and_artist:
                    string += item
                if ':' in string:
                    string_list = string.split(':')
                else:
                    string_list = string.split(',')
                artist = string_list[0]
                title = string_list[-1]
                connection.insert(artist, title)
        except:
            print("invild input(ex. a --artist <name> --title <title>)")

    elif args[1] == 'd':
        if args[2]:
            connection.delete(args[2])
        else:
            print("Please input the id of music you wanna play.")
    elif args[1] == 'p':
        if args[2]:
            print(f"play music No.{args[2]}")
            connection.play(args[2])
        else:
            print("Please input the id of music you wanna play.")
    else:
        print("invaild input")
        print("l for list, a for add, d for delete, p for play.")

    connection.close_database()

if __name__ == "__main__":
    main(sys.argv)