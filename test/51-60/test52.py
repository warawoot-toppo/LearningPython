'''
กำหนดให้ list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
เขียนโปรแกรมลบสมาชิกที่ index เป็นเลขคู่โดยใช้ remove จากนั้นให้พิมพ์ค่า list1 ออกมา
'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(list1)
for i in range(n - 1, -1, -1):
    if i % 2 == 0:
        list1.remove(list1[i])
print(list1)        
