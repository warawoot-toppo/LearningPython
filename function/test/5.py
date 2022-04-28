from pyrsistent import l


def mix_list(a, b):
    
    
    listA = [] 
    listB = []
    for i in range(len(a)):
        listA.append(a[i] + b[i])
        listB.append(a[i] * b[i])
    return listA, listB

listA, listB = mix_list([1,2,3], [4,5,6])
print(listA)
print(listB)   