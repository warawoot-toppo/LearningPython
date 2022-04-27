n = int(input(': '))
dict1 = {}
list1 = []
list2 = []

for i in range(n):
    str1 = input('str1: ')
    list1.append(str1)
    int1 = int(input('int1: '))
    list2.append(int1)

for i in range(len(list1)):
    if i % 2 == 0:    
        dict1[list1[i]] = list2[i]
    else:
        dict1[list2[i]] = list1[i]
    
print(dict1)
