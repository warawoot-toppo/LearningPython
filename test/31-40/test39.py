'''
เขียนโปรแกรมรับ input 1 ตัวที่เป็น str จากนั้นให้สร้าง str ถอยหลัง ของ input ที่รับและพิมพ์ออกมา
'''
str1 = input('str1: ')
n = len(str1)
a = ''
for i in range(n - 1, -1, -1):
    a = a + str1[i]
print(a)    