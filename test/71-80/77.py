dict2 = {'name' : 'Mario', 'age' : '30', 'job' : 'mushroom picker'}
str1 = input('str1: ')

if str1 in dict2.values():
    for k in dict2:
        if dict2[k] == str1:
            a = k
            break
    del dict2[a]        
else:
    dict2['new_key'] = str1
print(dict2)                