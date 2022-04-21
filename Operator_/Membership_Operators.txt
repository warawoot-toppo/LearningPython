'''
in     =  มีสมาชิกอยู่ใน...หรือไม่?
not in =  ไม่มีสมาชิกอยู่ใน...หรือไม่?
'''

listA = [1, 2, 3]
tupleA = ('a', 'b', 'c', 'd')

print(1 in listA)
print(1 in tupleA)

print(1 not in listA)
print(1 not in tupleA)

dictA = {'name' : 'John', 'age' : 32}
setA = {'Sushi', 'Salmon'}

print('name' in dictA)
print('Egg' in setA)

print('name' not in dictA)
print('Egg' not in setA)