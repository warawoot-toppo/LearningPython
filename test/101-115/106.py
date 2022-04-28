for i in range(7):
    for j in range(7):
        if (i == j) or (i + j == 6):
            print('x', end = '')
        else:
            print('-', end = '')
    print()               