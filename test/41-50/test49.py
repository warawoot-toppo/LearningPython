'''
กำหนดให้ list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] เขียนโปรแกรมรับ input 1 ตัวที่เป็น int
และให้ตรวจสอบว่า จำนวนที่รับมาเป็นสมาชิกของ list1 หรือไม่
- ถ้าเป็นให้ทำการลบจำนวนนั้นโดยใช้คำสั่ง del
- ถ้าไม่เป็นให้เพิ่มจำนวนนั้นโดยใช้ methon append
จากนั้นให้พิมพ์ค่า list1 ออกมา
'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
int1 = int(input('= '))
if int1 in list1:
    index = list1.index(int1)
    del list1[index]
else:
    list1.append(int1)  
print(list1)      