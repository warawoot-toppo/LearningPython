'''
กำหนดให้ vowel = ['a', 'e', 'i', 'o', 'u'] เขียนโปรแกรมรับ input 1 ตัวที่เป็น str (str1) 
ให้แทนที่ค่า str ในตำแหน่งที่มีใน vowel ปรากฎด้วย '*' จากนั้นให้พิมพ์ str ที่ผ่านกระบวนการดังกล่าวออกมา
'''
vowel = ['a', 'e', 'i', 'o', 'u']
str1 = input('str1: ')

for i in vowel:
    str1 = str1.replace(i, '*')
print(str1)        