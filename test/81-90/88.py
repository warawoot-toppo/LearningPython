

for i in range(5):
    float1 = float(input('= '))
    
    if i == 0:
        _max = float1
    else:
        if float1 > _max:
            _max = float1    
print(_max)        
