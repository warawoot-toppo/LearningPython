for i in range(10):
    for j in range(20):
        if (9 - i <= j) and (j <= 9 + i):
            print('x', end = '')
        else:
            print('-', end = '')
    print()            