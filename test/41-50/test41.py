'''
กำหนดให้ list3 = [1, 2, 3,..., 25] เขียนโปรแกรมเปลี่ยนสมาชิกใน list3 ที่ index 
เป็นเลขคู๋ให้เป็น 'a' จากนั้นให้พิมพ์ค่า list3 ออกมา
'''
list3 = [x for x in range(1, 26)]
n = len(list3)
for i in range(n):
    if i % 2 == 0:
        list3[i] = 'a'
print(list3)        