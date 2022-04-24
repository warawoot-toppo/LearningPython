'''
เขียนโปรแกรมรับ input 5 ตัวที่เป็น str โดยใช้ for loop จากนั้นให้นับความยาวรวมของ str ที่รับและพิมพ์ออกมา
'''
count = ''
for i in range(5):
    str1 = input('str1: ')
    count = count + str1
print(len(count))