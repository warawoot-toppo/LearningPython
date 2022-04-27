list1 = ['t', 'u', 'r', 'i', 'n', 'g']
tuple1 = tuple('newton')
set1 = set()
set2 = set()
for l in range(len(list1)):
    if l % 2 == 0:
        set1.add(list1[l])
        
for t in range(len(tuple1)):
    if t % 2 == 1:
        set2.add(tuple1[t]) 
   
print(set1)
print(set2)        