def exalt_list(listA):
    for i in range(len(listA)):
        listA[i] = listA[i] ** 2    
    return listA   

listA = [1, 2, 3, 4, 5]
print(exalt_list(listA))