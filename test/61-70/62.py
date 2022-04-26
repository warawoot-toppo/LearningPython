'''
กำหนดให้ tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) เขียนโปรแกรมหาผลบวกกำลัง 2 ของสมาชิกใน tuple1
ที่มี index เป็นเลขคี่ จากนั้นให้พิมพ์ผลลัพธ์ออกมา
'''
tuple1 = tuple(x for x in range(1, 11))
n = len(tuple1)
sumx = 0
for i in range(n):
    if i % 2 != 0:
        sumx += tuple1[i] ** 2
print(sumx)        