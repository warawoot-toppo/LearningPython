def min_max(listA):
    minA = listA[0]
    maxA = listA[0]
    n = len(listA)
    for i in range(n):
        if listA[i] < minA:
            minA = listA[i]
        if listA[i] > maxA:
            maxA = listA[i]
    return minA, maxA               

min1,max1 = min_max([1, 2, 3])
print(min1)
print(max1)            
    
