'''
เขียนโปรแกรมรับ input 1 ตัวที่เป็น str จากนั้นให้พิมพ์ str ที่ index เป็นเลขคี่
'''
str1 = input('str1: ')
for i in range(len(str1)):
    if i % 2 != 0:
        print(str1[i])