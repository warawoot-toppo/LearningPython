'''
กำหนดให้ list2 = ['a', 'l', 'l', 'i', 'g', 'a', 't', 'o', 'r'] 
เขียนโปรแกรมรับ input 1 ตัวที่เป็น str ให้ตรวจสอบว่า str ที่รับมามีค่าตรงกับสมาชิกตำแหน่งใดใน list2
และพิมพ์ออกมา
'''
list2 = list('alligator')
str1 = input('str1: ')
for i in range(len(list2)):
    if list2[i] == str1:
        print(i)