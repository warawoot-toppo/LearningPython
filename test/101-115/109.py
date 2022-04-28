for i in range(10):
    for j in range(10):
        if j < 9 - i:
            print('-', end = '')
        else:
            print('x', end = '')     
        
    print()    
