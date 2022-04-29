def shift_right(listA,k):
    k = k % len(listA)
    return listA[-k:] + listA[:-k]

print(shift_right([1, 2, 3, 4],4))