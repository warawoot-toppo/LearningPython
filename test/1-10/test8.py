'''
กำหนดให้ list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] เขียนโปรแกรมสร้าง list ถอยหลังของ
list1 และพิมพ์ออกมา
'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
n = len(list1)
for i in range(n - 1, -1, -1):
    list2.append(list1[i])
print(list2)    