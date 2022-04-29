def distance_Rn(p1,p2):
    sum_square = 0
    n = len(p1)
    for i in range(n):
        sum_square += (p1[i] - p2[i]) ** 2
    distance = sum_square ** (1/2)
    return distance



print(distance_Rn((1, 2, 2, 1), (3, 4, 0, -1)))        