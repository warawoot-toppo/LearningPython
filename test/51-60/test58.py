'''
กำหนดให้ matrix1 = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
เขียนโปรแกรม transpose matrix1 และพิมพ์ผลลัพธ์ออกมา
'''
matrix1 = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]]
tran_matrix = [[0, 0, 0],  
               [0, 0, 0], 
               [0, 0, 0]]
n_rows = len(matrix1)
n_cols = len(matrix1[0])
for r in range(n_rows):
    for c in range(n_cols):
        tran_matrix[c][r] = matrix1[r][c]
print(tran_matrix)