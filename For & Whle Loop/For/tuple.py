tuplex = ('a', 'b', 'c', 'd', 'e')
n = len(tuplex)
for i in range(n):
    print(tuplex[i])

print('-------------------------')

for i in range(len(tuplex)):
    print(tuplex[i]) 

print('-------------------------')

for i in tuplex:
    print(i) 

print('-------------------------')

for i, c in enumerate(tuplex):
    print(i, c)    