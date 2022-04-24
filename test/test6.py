'''
เขียนโปรแกรมสร้าง empty list (list1) และรับ input 5 ตัวที่เป็นจำนวนเต็ม
โดยใช้ for loop และให้ตรวจสอบว่า จำนวนที่รับยังไม่เป็นสมาชิกของ list1 หรือไม่
- ถ้ายังไม่เป็นสมาชิกให้ append จำนวนนั้นเข้าไปใน list1
- ถ้าเป็นสมาชิกอยู่แล้ว ไม่ดำเนินการใดๆ
จากนั้นให้พิมพ์ค่า list1 ออกมา
'''
list1 = []
for i in range(5):
    int1 = int(input('int1= '))
    if int1 not in list1:
        list1.append(int1)
   
print(list1)        

