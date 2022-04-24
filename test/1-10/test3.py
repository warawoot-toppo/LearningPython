'''
เขียนโปรแกรมรับ input 1 ตัวที่เป็น str จากนั้นให้ทำการหา str ที่แตกต่างกันทั้งหมด
พร้อมทั้งจำนวนครั้งที่ str นั้นๆปรากฎและพิมพ์ออกมา
'''
str1 = input('str1: ')
set1 = set(str1)
for s in set1:
    count_s = str1.count(s)
    print(s, count_s)
