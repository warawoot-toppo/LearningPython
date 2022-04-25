'''
กำหนดให้ listx = [0, 2, 4, 6, 8] และ list4 = ['a', 'b', 'c', 'd', 'e', 'f']
เขียนโปรแกรมแทรก '*' ไปใน list4 ใน index ที่เป็นสมาชิกของ listx
'''
listx = [0, 2, 4, 6, 8]
list4 = ['a', 'b', 'c', 'd', 'e', 'f']
n = len(listx)
for i in range(n):
    list4.insert(listx[i], '*')

print(list4)        
    