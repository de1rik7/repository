import random
def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def move_max_to_corner(matrix):
    n = len(matrix)
    m = len(matrix[0])

    max_val = matrix[0][0]
    max_i, max_j = 0, 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_i, max_j = i, j

    result = [row[:] for row in matrix]

    if max_i != 0:
        result[0], result[max_i] = result[max_i], result[0]

    if max_j != 0:
        for i in range(n):
            result[i][0], result[i][max_j] = result[i][max_j], result[i][0]

    return result, max_val

print("ЗАДАЧА 1")
matrix1 = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
print("Матрица для проверки:")
for row in matrix1:
    print(row)

if is_symmetric(matrix1):
    print(" Матрица симметрична")
else:
    print(" Матрица не симметрична")