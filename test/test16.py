'''
เขียนโปรแกรมพิมพ์จำนวนที่หารด้วย 3, 5 และ 7 ลงตัว ซึ่งอยู่ระหว่าง 0 ถึง 100
'''
for i in range(1, 1000):
    if (i % 3 == 0) and (i % 5 == 0) and (i % 7 == 0):
        print(i)