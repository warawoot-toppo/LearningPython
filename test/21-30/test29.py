'''
เขียนโปรแกรมหาจำนวนเฉพาะที่อยู่ระหว่าง 0 ถึง 100 และพิมพ์ออกมา
'''
for j in range(1, 100):
    c = 0
    for i in range(1, j + 1):
        if j % i == 0:
            c = c +1
    if c == 2:
        print(j)        
