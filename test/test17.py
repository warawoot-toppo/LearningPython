'''
เขียนโปรแกรมพิมพ์จำนวนที่หารด้วย 3, 5 หรือ 7 ลงตัว ซึ่งอยู่ระหว่าง 0 ถึง 100
'''
for i in range(1,100):
    if (i % 3 == 0) or (i % 5 == 0) or (i % 7 == 0):
        print(i)