def sum_list(listA):
    sumx = 0
    for i in range(len(listA)):
        sumx += listA[i]
    return sumx
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

print(sum_list(list1))
print(sum_list(list2))