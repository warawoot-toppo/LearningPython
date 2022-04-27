list1 = []
for i in range(5):
    float1 = float(input('= '))
    list1.append(float1)
    if i == 0:
        _max = float1
    else:
        if float1 > _max:
            _max = float1    

print(_max)
print(list1.count(_max))   