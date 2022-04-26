'''
กำหนดให้ tuple2 = (1, 2, 3,..., 25) เขียนโปรแกรมหาค่าเฉลี่ยของจำนวนเฉพาะใน tuple2 และพิมพ์ออกมา
'''
tuple2 = tuple(x for x in range(1, 26))
a = 0
b = 0
for i in tuple2:
    c = 0
    for j in range(1, i + 1):
        if i % j == 0:
            c = c + 1
    if c == 2:
        a = a + i
        b = b + 1        
g = a / b
print(g)