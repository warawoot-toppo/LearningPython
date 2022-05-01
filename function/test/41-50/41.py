def draw_tree2(n):
    if n % 2 == 0:
        for i  in range(n - 1):
            for j in range(n):
                if (j == abs(int((n - 1) / 2) - i)) or (j == n - 1 - abs(int((n - 1) / 2) - i)):
                    print('x', end = '')
                else:
                    print('-', end = '')
            print()
    else:
        for i in range(n):
            for j in range(n):
                if (j == abs((n - 1) / 2 - i)) or (j == n - 1 - abs((n - 1) / 2 - i)):
                    print('x', end = '')
                else:
                    print('-', end = '')
            print()

draw_tree2(12)

