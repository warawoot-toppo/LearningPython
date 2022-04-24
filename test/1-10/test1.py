'''
เขียนโปรแกรมรับ input 2 ตัวที่เป็น str และ int ตามลำดับ (str1, int1) 
ถ้าความยาวของ str1 น้อยกว่า int1 ให้ทำการต่อ str1 ด้วย '*'
จนกว่าความยาวของ str1 จะเท่ากับ int1 สุดท้ายให้พิมพ์ค่า str1 
ที่ผ่านกระบวนการดังกล่าวออกมา
'''
str1 = input('str1: ')
int1 = int(input('int1: '))
while len(str1) < int1:
    str1 = str1 + '*'
print(str1)
