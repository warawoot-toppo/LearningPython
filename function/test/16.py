def length_list(listA):
    a = 0

    for i in listA:
        a = a + len(i)
    return a    

listA = ['a', 'ab', 'abc', 'abcd']

print(length_list(listA))