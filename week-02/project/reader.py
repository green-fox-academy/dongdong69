import csv

def reader():
    csvr = open('dongdong69\week-02\project\logs.csv', encoding="utf-8", mode="r")

    records_dic_list = []
    lines = csv.reader(csvr)
        
    for line in lines:
        record_dic = {}
        #the number of the line which can be useful when loading information
        record_dic["number"] = line[0]
        #the date
        record_dic["date"] = line[1][:10]
        #the specific time door opens
        record_dic["time"] = time_to_sec(line[1][12:])
        #the name of the door
        record_dic["door"] = line[5]
        #the name of stuff
        record_dic["name"] = line[7]
        #the id of stuff
        record_dic["id"] = line[12]
        #add into the recordsList
        records_dic_list.append(record_dic)

    return(records_dic_list)

def time_to_sec(time):
    ##time to sec : 09:00:00 to 32400
    time_list = time.split(':')
    h, m, s = time_list[0], time_list[1], time_list[2]

    return float(h)*3600 + float(m)*60 + float(s)