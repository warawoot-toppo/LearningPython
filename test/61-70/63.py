'''
กำหนดให้ tuple2 = (1, 2, 3,...,25) เขียนโปรแกรมหาจำนวนเฉพาะใน tuple2 และพิมพ์ออกมา
'''
tuple2 = tuple(x for x in range(1, 26))

count = 0
for i in tuple2:
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count = count + 1
    if count == 2: 
         print(i)