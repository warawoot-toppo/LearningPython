for i in range(10):
    for j in range(10 + i):
        if j > 8 - i:
            print('x', end = '')
        else:
            print('-', end = '')
    print()            