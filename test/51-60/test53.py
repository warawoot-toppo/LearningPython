'''
กำหนดให้ list3 = [1, 2, 3,..., 25] เขียนโปรแกรม][สมาชิกใน list3
ที่ค่าถูกหารด้วย 2 หรือ 3 ลงตัวเพียงตัวใดตัวหนึ่งโดยใช้คำสั่ง del
จากนั้นให้พิมพ์ค่า list3 ที่ผ่านกระบวนการดังกล่าวออกมา
'''
list3 = [x for x in range(1, 26)]
n = len(list3)
for i in range(n - 1, -1, -1):
    if list3[i] % 2 == 0:
        if list3[i] % 3 != 0:
            del list3[list3[i]]
    else:
        if list3[i] % 3 == 0:
            del list3[list3[i]]
print(list3)                    