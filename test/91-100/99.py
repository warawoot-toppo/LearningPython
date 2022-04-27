dict1 = {}
list1 = []
for i in range(5):
    float1 = float(input('= '))
    list1.append(float1)
set1 = set(list1)
for s in set1:
    dict1[s] = list1.count(s) 
    
isfirstkey = True
for key in dict1:
    if isfirstkey == True:
        _max = dict1[key]
        isfirstkey = False
    else:
        if dict1[key] > _max:
            _max = dict1[key]
for i in dict1:
    if dict1[i] == _max:
        print('ฐานนิยมคือ:',i)             