'''
เขียนโปรแกรมรับ input 5 ตัวที่เป็น str โดยใช้ for loop จากนั้นให้ตรวจสอบว่าใน str ที่รับมาทั้งหมดมี 'a' ปรากฎกี่ครั้ง
และพิมพ์ออกมา
'''
count = 0
for i in range(5):
    str1 = input('str1: ')
    n = str1.count('a')
    count = count + n
print(count)