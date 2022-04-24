'''
เขียนโปรแกรมสร้าง empty list และรับ input ที่เป็น str และ append เข้าไปใน list 
จนกว่าความยาวของ list จะเท่ากับ 5 โดยมีเงื่อนไขว่าถ้า str ที่รับเป็นสมาชิกใน list อยู่แล้ว
จะไม่ทำการ append
'''
list1 = []
n = 1
while len(list1) < 5:
    str1 = input('str1ตัวที่ ' + str(n) + ' : ')
    if str1 not in list1:
        list1.append(str1)
    n = n + 1    
print(list1)    