'''
กำหนดให้ list3 = [1, 2, 3,..., 25] เขียนโปรแกรมลบสมาชิกใน list3
ที่ค่าถูกหารด้วย 2 ลงตัวแต่หารด้วย 3 ไม่ลงตัวโดยใช้ remove
จากนั้นให้พิมพ์ค่า list3 ที่ผ่านกระบวนการดังกล่าวออกมา
'''
list3 = [x for x in range(1, 26)]
n = len(list3)
for i in range(n - 1, -1, -1):
    if (list3[i] % 2 == 0) and (list3[i] % 3 != 0):
            list3.remove(list3[i])
print(list3)