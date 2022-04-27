dict1 = {}
list1 = []
for i in range(5):
    float1 = float(input('= '))
    list1.append(float1)
set1 = set(list1)
for s in set1:
    dict1[s] = list1.count(s) 
    
print(dict1)