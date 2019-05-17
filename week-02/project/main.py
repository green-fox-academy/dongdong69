from reader import reader
from first_arrive import first_arrive

#the records list which contain the information about
#
#number : string
#date : string
#specific time : float
#door : string
#name : string
#id : string
records_dic_list = reader()

# the set of doors
doors = set()
dates = set()
for record in records_dic_list:
    dates.add(record["date"])
    doors.add(record["door"])

#the id of different doors
door_dic = {}
for door in doors:
    door_dic[door[:8]] = door[8:]

print(door_dic)

#the record of the different time of different people's first arrive
first_arrive_record = first_arrive(records_dic_list)
print(first_arrive_record['Czender András'])

#there are 193 different people in Green Fox
#print(len(first_arrive_record))