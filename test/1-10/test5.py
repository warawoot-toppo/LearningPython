'''
เขียนโปรแกรมสร้าง empty list และ append ค่า 99, 98, 97,..., 80 ลงไปใน list นั้น
หลังจากนั้นให้พิมพ์ค่า list ที่สร้างออกมา
'''
list1 = []
for i in range(99, 79, -1):
    list1.append(i)
print(list1)    