def isPrime_list(lista):
    list1 = []

    for j in lista:
        
        count = 0
        for i in range(1,j+1):
            if j % i == 0:
                count += 1
        
        if count == 2:
            list1.append(True)
        else:
            list1.append(False)
    return list1

print(isPrime_list([3, 3, 5, 2, 3, 7, 8, 9]))    




           
        


#print(isPrime_list([1, 2, 3, 4, 5]))               


