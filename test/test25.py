'''
เขียนโปรแกรมรับอินพุต 5 ตัวที่เป็นจำนวนจริงโดยใช้ for loop จากนั้นให้หาผลคูณของจำนวนที่เป็นบวก
และพิมพ์ผลลัพธ์ออกมา
'''
sumx = 1
for i in range(5):
    float1 = float(input('= '))
    if float1 > 0:
        sumx = sumx * float1
print(sumx)        
