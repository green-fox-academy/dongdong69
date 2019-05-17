def first_arrive(records):
    #recording the first arrival time for different in different day
    first_arrive_dic = {}
    for record in records:
        if record["name"] not in first_arrive_dic:
            first_arrive_dic[record["name"]] = {record["date"] : [record["time"], record["door"][:8]]}
        elif record["date"] not in first_arrive_dic[record["name"]]:
            first_arrive_dic[record["name"]][record["date"]] = [record["time"], record["door"][:8]]

    return first_arrive_dic