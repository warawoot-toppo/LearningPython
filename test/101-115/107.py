for i in range(7):
    for j in range(7):
        if (j == abs(3 - i)) or (j == 6 - abs(3 - i)):
            print('x', end = '')
        else:
            print('-', end = '')
    print()            
