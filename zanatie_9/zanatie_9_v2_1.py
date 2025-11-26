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

print("ЗАДАЧА 1")
magic_sq = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
print("Матрица для проверки:")
for row in magic_sq:
    print(row)

if is_magic_square(magic_sq):
    print(" Это магический квадрат!")
else:
    print(" Это НЕ магический квадрат!")