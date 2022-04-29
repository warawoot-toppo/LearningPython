def position(listA, k):
    if k in listA:
        for i in range(len(listA)):
            if listA[i] == k:
                return i
    else:
        return -1   

print(position([2,4,6,8,12],7))