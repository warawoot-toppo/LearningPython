char = 'Python'
n = len(char)
for i in range(n):
    print(char[i])

print('-------------------------')

for i in range(len(char)):
    print(char[i]) 

print('-------------------------')

for i in char:
    print(i) 

print('-------------------------')

for i, c in enumerate(char):
    print(i, c)    