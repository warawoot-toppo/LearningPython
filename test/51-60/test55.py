'''
กำหนดให้ list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] เขียนโปรแกรมรับ input 1 ตัวที่เป็น int
และตรวจสอบว่าจำนวนที่รับมาเป็นสมาชิกใน list1 หรือไม่
- ถ้าเป็นให้ทำการลบสมาชิกโดยใช้ remove
- ถ้าไม่เป็น ไม่ดำเนินการใดๆ
'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


while len(list1) != 7:
    int1 = int(input('= '))
    if int1 in list1:
        list1.remove(int1)
        
print(list1)    