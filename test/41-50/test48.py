'''
กำหนดให้ list4 = ['a', 'b', 'c', 'd', 'e', 'f']
เขียนโปรแกรมรับ input 1 ตัวที่เป็น str (str1) จากนั้นให้ตรวจสอบว่า str1 เป็นสมาชิกของ list4 หรือไม่
- ถ้าเป็นให้ทำการลบ str1 ออกจาก list4 โดยใช้ method remove
- ถ้าไม่เป็นไม่ดำเนินการใดๆ
'''
list4 = ['a', 'b', 'c', 'd', 'e', 'f']
str1 = input('str1: ')
n = len(str1)
for i in range(n):
    if str1[i] in list4:
        list4.remove(str1[i])
print(list4)        