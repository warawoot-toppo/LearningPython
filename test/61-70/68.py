'''
กำหนดให้ tuple1 = (1, 2, 3, 4) และ tuple2 = ('ant', 'bird', 'cat', 'dog')
เขียนโปรแกรมสร้าง dictionary ที่มี key เป็นสมาชิกใน tuple1 และมี value เป็นสมาชิกใน tuple2
ที่ index ตรงกัน เชจากนั้นให้พิมพ์ค่า dictionary ที่สร้างออกมา
'''
tuple1 = (1, 2, 3, 4)
tuple2 = ('ant', 'bird', 'cat', 'dog')
dict1 = {}
for i in range(len(tuple1)):
    dict1[tuple1[i]] = tuple2[i]
print(dict1)    