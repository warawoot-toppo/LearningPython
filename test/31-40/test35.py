'''
เขียนโปรแกรมรับ input 2 ตัวที่เป็น str (str1, char1) ให้ตรวจสอบความยาวของ char1 ว่าเป็น 1 หรือไม่
- ถ้าความยาวเป็น 1 ให้ตรวจสอบว่า char1 ปรากฎที่ index ใดบ้างของ str1 และพิมพ์ออกมา
- ถ้าความยาวไม่เป็น 1 ไม่ดำเนินการใดๆ
'''
str1 = input('str1: ')
char1 = input('char1 ')
if len(char1) == 1:
    n = len(str1)
    for i in range(n):
        if str1[i] == char1:
            print(i)