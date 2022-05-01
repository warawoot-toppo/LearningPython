def del_exceed_len(listA, n):
    remain_list = []
    for a in listA:
        if len(a) <= n:
            remain_list.append(a)
    return remain_list

print(del_exceed_len(['Hello', 'Hel', 'Hell', 'He', 'H'],3))