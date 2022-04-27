dict1 = {'apple' : '52 kcal', 'banana' : '132 kcal', 'carrot' : '46 kcal'}
str1 = input('str1: ')
if str1 in dict1:
    dict1[str1] = 'wait for new value'
else:
    dict1[str1] = 'wait for assignment'
print(dict1)    