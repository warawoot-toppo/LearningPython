def coin(am):
    list1 = ['1000', '500', '100', '50', '10', '5', '2', '1']
    dict1 = {'1000' : 0, '500' : 0, '100' : 0, '50' : 0, '10' : 0, '5' : 0, '2' : 0, '1' : 0}
    for i in list1:
        if am != 0:
            a = am // int(i)
            dict1[i] = a
            am -= a * int(i)
    return dict1


print(coin(58))
            