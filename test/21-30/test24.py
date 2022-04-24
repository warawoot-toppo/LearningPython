'''
เขียนโปรแกรมรับอินพุต 5 ตัวที่เป็นจำนวนจริงโดยใช้ for loop จากนั้นให้หาผลรวมของจำนวนที่เป็นบวกและจำนวนที่เป็นลบ
สุดท้ายให้พิมพ์ผลลัพธ์ออกมา
'''
a = 0
b = 0
for i in range(5):
    float1 = float(input('= '))
    if float1 > 0:
        a = a + float1
    else:
        b = b + float1
print(a)
print(b)            
