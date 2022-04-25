'''
กำหนดให้ list4 = ['a', 'b', 'c', 'd', 'e', 'f'] 
เขียนโปรแกรมรับ index และ element ที่จะแทรกใน list จำนวน 3 ครั้ง
โดยใช้ for loop โดยมีเงื่อนไขว่าจะทำการแทรกก็ต่อเมื่อ element ยังไม่เป็นสมาชิกของ list4 เท่านั้น
จากนั้นให้พิมพ์ค่า list4 ที่ผ่านกระบวนการดังกล่าวออกมา
'''
list4 = ['a', 'b', 'c', 'd', 'e', 'f']
for i in range(3):
    index = int(input('= '))
    element = (input('= '))
    if element not in list4:
        list4.insert(index, element)
print(list4)        