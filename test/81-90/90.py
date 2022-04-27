country = ['Brazil', 'China', 'Germany', 'Japan', 'Sweden']
dict1 = {}
for i in range(len(country)):
    income = float(input(country[i] + '\'s income : '))
    dict1[country[i]] = income
    if i == 0:
        _max = income
    else:
        if income > _max:
            _max = income
for key in dict1:
    if dict1[key] == _max:
        print(key + ' : ' + str(dict1[key]))                
 
           