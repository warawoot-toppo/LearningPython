'''
กำหนดให้ matrix1 = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
และ matrix2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
เขียนโปรแกรมหาผลคูณของสมาชิกในตำแหน่งที่ตรงกันของ matrix1 และ matrix2
จากนั้นให้พิมพ์ผลลัพธ์ในรูปแบบของ list 2 มิติออกมา
'''
matrix1 = [[1, 2, 3], 
           [4, 5, 6],
           [7, 8, 9]]
matrix2 = [[1, 2, 3], 
           [1, 2, 3], 
           [1, 2, 3]]
result_matrix = [[0, 0, 0], 
                 [0, 0, 0], 
                 [0, 0, 0]]
n_rows = len(matrix1)
n_cols = len(matrix1[0])
for r in range(n_rows):
    for c in range(n_cols):
        result_matrix[r][c] = matrix1[r][c] * matrix2[r][c]
print(result_matrix) 