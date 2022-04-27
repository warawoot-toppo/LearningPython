list1 = []
for i in range(5):
    float1 = float(input('float: '))
    list1.append(float1)
    if i == 0:
        _min = float1
    else:
        if float1 < _min:
            _min = float1
print(_min)
print(list1.count(_min))                