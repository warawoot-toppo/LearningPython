for i in range(9):
    n = 1
    for j in range(9):
        if j < 8-i:
            print('-', end = '')
            
        else:
            print(n, end = '')   
            n += 1 
    print()        