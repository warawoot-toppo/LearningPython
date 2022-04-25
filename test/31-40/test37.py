'''
กำหนดให้ vowel = ['a', 'e', 'i', 'o', 'u'] เขียนโปรแกรมรับ input 1 ตัวที่เป็น str 
จากนั้นให้ตรวจสอบว่า str ที่รับมามีสมาชิกใน vowel ปรากฎหรือไม่
- ถ้ามีให้พิมพ์ 'There is vowel'
- ถ้าไม่มีให้พิมพ์ 'There is no vowel'
'''
vowel = ['a', 'e', 'i', 'o', 'u']
str1 = input('str1: ')
n = False
for i in vowel:
    if i in str1:
        n = True
        break
if n == True:
    print('There is vowel')
else:
    print('There is no vowel')            



