def reshape(listA, dim):
    old_n = len(listA)
    new_n = dim[0] * dim[1]
    matrixA = []
    if old_n == new_n:
        row = dim[0]
        col = dim[1]
        for i in range(row):
            matrixA.append(listA[i * col : (i + 1) * col])
        return matrixA
    else:
        print('invalid dimension')   


print(reshape([x for x in range(1, 13)], (4,3)))