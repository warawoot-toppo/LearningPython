'''
เขียนโปรแกรมรับอินพุต 5 ตัวที่เป็นจำนวนเต็มโดยใช้ for loop 
จากนั้นให้หาผลรวมของจำนวนที่รับและพิมพ์ออกมา
'''
sumx = 0
for i in range(5):
    int1 = int(input('int1: '))
    sumx = sumx + int1
print(sumx)    
