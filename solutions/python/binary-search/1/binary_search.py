def find(search_list, value):
    len_list = len(search_list)
    out= search_list
    pos =0 
    found = False
    while (len_list>0 and pos <= 0):
        middle = (len_list//2)
        if (search_list[middle] == value):
            pos=1
        elif (search_list[middle] > value):
            search_list = search_list[:middle]
        else:
            search_list = search_list[middle:]
        len_list = len(search_list)
        if (len(search_list) == 1 and (search_list[0] != value)):
            pos=2

    if pos == 1:
        return out.index(value)
    else:
        raise ValueError("value not in array")