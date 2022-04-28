def draw():
    for i in range(4):
        for j in range(4 + i):
            if i + j >= 3:
                print('x', end = '')
            else:
                print('-', end = '')
        print()



draw()
