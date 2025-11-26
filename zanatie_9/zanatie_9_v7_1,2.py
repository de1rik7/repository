import random
def restore_symmetric_matrix(upper_triangle, n):
    matrix = [[0] * n for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = upper_triangle[idx]
            matrix[j][i] = upper_triangle[idx]
            idx += 1
        return matrix
def matrix_trace_transform(matrix):
    n = len(matrix)
    trace = sum(matrix[i][i] for i in range(n))
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(x / trace for x in matrix[i])
        else:
            result.append(matrix[i][:])
    return result, trace

print('Задача 1')
n = 3
upper_tri = [1, 2, 3, 4, 5, 6]
print(f'Верхний треугольник: {upper_tri}')

matrix = restore_symmetric_matrix(upper_tri, n)
print('Восстановленная матрица:')
for row in matrix:
    print(row)

print('\nЗадача 2')
n = 3
matrix =[[random.randint(1, 5) for _ in range(n)] for _ in range(n)]
print("Исхожная матрица:")
for row in matrix:
    print(row)

new_matrix, trace = matrix_trace_transform(matrix)
print(f'Следующая матрица: {trace}')
print('Преобразованная матрица:')
for row in new_matrix:
    print(f'{x:.3f}' for x in row)