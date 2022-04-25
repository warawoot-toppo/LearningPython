'''
กำหนดให้ list4 = ['a', 'b', 'c', 'd', 'e', 'f']
เขียนโปรแกรมรับ index และ element ที่จะแทรกใน list จำนวน 3 ครั้ง
โดยใช้ for loop จากนั้นให้พิมพ์ค่า list4 ที่ผ่านกระบวนการดังกล่าวออกมา
'''
list4 = ['a', 'b', 'c', 'd', 'e', 'f']
for i in range(3):
    index = int(input('= '))
    element = int(input('= '))
    list4.insert(index, element)
print(list4)    