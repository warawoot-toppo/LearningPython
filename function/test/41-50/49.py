def derivative(listA):
    n = len(listA)
    diff = [0] * n
    for i in range(1, n):
        diff[i - 1] = listA[i] * i
    return diff

print(derivative([2, 3, 0, 1]))