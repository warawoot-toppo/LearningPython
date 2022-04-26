'''
กำหนดให้ list1 = ['one', 'two', 'three', 'four'] และ 
list2 = [1, 2, 3, 4] เขียนโปรแกรมสร้าง dictionary ที่มี key เป็นสมาชิกใน list1 และมี value 
เป็นสมาชิกใน list2 ที่ index ตรงกัน จากนั้นให้พิมพ์ค่า dictionary ที่สร้างออกมา
'''
list1 = ['one', 'two', 'three', 'four']
list2 = [1, 2, 3, 4] 
dict1 = {}
for i in range(len(list1)):
    dict1[list1[i]] = list2[i]
print(dict1)