for i in range(10):
    for j in range(10, i , - 1):
        if j > 1 + i:
            print('-', end = '')
        else:
            print('x', end = '')
    print()            