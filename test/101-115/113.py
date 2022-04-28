for i in range(9):
    n = 0
    for j in range(9 + i):
        if i + j >= 8 and j <= 8:
            n += 1
            print(n, end = '')
        elif i + j >= 8 and j > 8:
            n -= 1
            print(n, end = '')  
        else:
            print('-', end = '')      
        
    print()        