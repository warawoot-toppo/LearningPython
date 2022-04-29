def shift_left(listA, k):
    k = k % len(listA)
    return listA[k:] + listA[:k]

print(shift_left([1, 2, 3, 4, 5],2))