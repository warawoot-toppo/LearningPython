'''
กำหนดให้ list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] เขียนโปรแกรมพิมพ์สมาชิกใน list1
ที่มี index เป็นเลขคู่
'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = 0
for i in range(len(list1)):
    if i % 2 == 0:
        
        print(list1[i])