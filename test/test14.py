'''
เขียนโปรแกรมพิมพ์จำนวนที่หารด้วย 3 และ 5 ลงตัว ซึ่งอยู่ระหว่าง 0 ถึง 100
'''
for i in range(1,100):
    if (i % 3 == 0) and (i % 5 == 0):
        print(i)