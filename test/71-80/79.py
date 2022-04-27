dict1 = {}
while len(dict1) != 3:
    str1 = input('str1: ')
    if str1 in dict1.keys():
        del dict1[str1]
    else:
        int1 = int(input('int1: '))
        dict1[str1] = int1
print(dict1)        