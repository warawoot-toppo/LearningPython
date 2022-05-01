def plus_and_cross(listA, listB):
    plus_list = []
    cross_list = []
    n = len(listA)
    for i in range(n):
        plus_list.append(listA[i] + listB[i])
        cross_list.append(listA[i] * listB[i])
    return plus_list, cross_list
plus, cross = plus_and_cross([1, 2, 3], [6, 7, 8])

print(plus)
print(cross)
