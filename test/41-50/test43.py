'''
กำหนดให้ list3 = [1, 2, 3,..., 25] เขียนโปรแกรมเปลี่ยนสมาชิกใน list3
ที่ค่าสามารถถอดรากที่ 2 แล้วเป็นจำนวนเต็มให้เป็น 'square' จากนั้นให้พิมพ์ค่า list3 ออกมา
'''
list3 = [x for x in range(1, 26)]
n = len(list3)
for i in range(n):
    if (list3[i] ** 0.5) % 1 == 0:
        list3[i] = 'square'
print(list3)        