def draw_tree(n):
    for i in range(n):
        for j in range(n):
            if (i == j) or (i + j == n - 1):
                print('x', end = '')
            else:
                print('-', end = '')
        print()        

draw_tree(11)