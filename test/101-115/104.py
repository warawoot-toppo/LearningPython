for i in range(4):
    for j in range(4 + i):
        if j < 3 - i:
            print('-', end = '')
        else:
            print('x', end = '')
    print()        
