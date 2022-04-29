def plus_ex(listA):

    b = 0
    for i in listA:
        a = i ** 2
        b = b + a
    return b

listA = [2, 2, 2]

print(plus_ex(listA))