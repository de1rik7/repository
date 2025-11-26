import random

def is_magic_square(matrix):
    n = len(matrix)

    magic_sum = sum(matrix[0])

    for i in range(n):
        if sum(matrix[i]) != magic_sum:
            return False

    for j in range(n):
        col_sum = sum(matrix[i][j] for i in range(n))
        if col_sum != magic_sum:
            return False

    return True
def swap_first_last_columns(matrix):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        matrix[i][0], matrix[i][m - 1] = matrix[i][m - 1], matrix[i][0]

    return matrix

print("\nЗАДАЧА 2")
n, m = 3, 4
matrix = [[random.randint(1, 9) for _ in range(m)] for _ in range(n)]
print("Исходная матрица:")
for row in matrix:
    print(row)

swapped_matrix = swap_first_last_columns([row[:] for row in matrix])
print("После перестановки столбцов:")
for row in swapped_matrix:
    print(row)