for i in range(4):
    for j in range(7 - i):
        if j < i:
            print('-', end = '')
        else:
            print('x', end = '')
    print()
             
