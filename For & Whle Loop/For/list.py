listx = ['a', 'b', 'c', 'd', 'e']
n = len(listx)
for i in range(n):
    print(listx[i])

print('-------------------------')

for i in range(len(listx)):
    print(listx[i])

print('-------------------------')

for i in listx:
    print(i)

print('-------------------------')

for i, c in enumerate(listx):
    print(i, c)