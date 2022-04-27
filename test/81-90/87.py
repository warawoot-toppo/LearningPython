set1 = set()
set2 = set()
while len(set1) < 3:
    str1 = input('str1: ')
    set1.add(str1)
while len(set2) < 3:
    str2 = input('str2: ')
    set2.add(str2)
print(set1 - set2)
print(set2 - set1)    