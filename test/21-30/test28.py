'''
เขียนโปรแกรมรับอินพุต 1 ตัวที่เป็นจำนวนเต็มบวก หลังจากนั้นให้ตรวจสอบว่าจำนวนที่รับมาเป็นจำนวนเฉพาะหรือไม่
- ถ้าเป็นให้พิมพ์ 'is prime'
- ถ้าไม่เป็นให้พิมพ์ 'is not prime'
'''
int1 = int(input('= '))
count = 0
for i in range(1, int1 + 1):
    if int1 % i == 0:
        count = count + 1
if count == 2:
    print('is prime')
else:
    print('is not prime')    