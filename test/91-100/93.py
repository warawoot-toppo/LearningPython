country = ['Brazil', 'China', 'Germany', 'Japan', 'Sweden']
dict1 = {}
for i  in range(len(country)):
    income = float(input(country[i] + ' : '))
    dict1[country[i]] = income
    if i == 0:
        _min = income
    else:
        if income < _min:
            _min = income
print()
for d in dict1:
    if dict1[d] == _min:
        print(d + ' : ' + str(_min))
          
