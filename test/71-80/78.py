dict2 = {'name' : 'Mario', 'age' : '30', 'job' : 'mushroom picker'}
list1 = ['firstname', 'lastname', 'age', 'job']
for i in list1:
    if i in dict2:
        del dict2[i]
print(dict2)        