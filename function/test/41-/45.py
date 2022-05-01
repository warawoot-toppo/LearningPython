def find_cusum(listA):
    cusum = 0
    cusum_list = []
    n = len(listA)
    for i in range(n):
        cusum += listA[i]
        cusum_list.append(cusum)
    return cusum_list

print(find_cusum([8, 0, -2, 4]))
