n = int(input('= '))
dict1 = {}
list1 = []
list2 = []
for i in range(n):
    str1 = input('str1: ')
    list1.append(str1)
    int1 = int(input('= '))
    list2.append(int1)
for j in range(len(list1)):
    dict1[list1[j]] = list2[j]


print(dict1)  
