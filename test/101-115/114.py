for i in range(5):
    if i % 2 == 0:
        n = 2 * i + 1
        for j in range(5 + i):
            if i + j >= 4:
                print(n, end = '')
                n -= 1
            else:
                print('-', end = '')
    else:
        n = 1
        for j in range(5 + i):
            if i + j >= 4:
                print(n, end = '')
                n += 1
            else:
                print('-', end = '')
                
    print()                
    
                            
