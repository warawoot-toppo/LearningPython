def sum_list(listA):
    a = 0
    for i in listA:
        if type(i) == int:
            a = a + i
    return a

listA = [1, 2.5, 3, 4.5, 5]

print(sum_list(listA))