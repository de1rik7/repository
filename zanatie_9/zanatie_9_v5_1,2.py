import random

def task_simple():
    n, m = 3, 4
    matrix = [[random.randint(-1, 10) for j in range(m)] for i in range(n)]

    print('Исходная матрица:')
    for row in matrix:
        print(row)

    for i in range(n):
        matrix[i].sort()
    print('\nПосле сортировки строк:')
    for row in matrix:
        print(row)

def task2_simple():
    n, m = 3, 4
    numders = random.sample(range(1, 50), n*m)
    matrix = [numders[i*m:(i+1)*m] for i in range(n)]

    print('\nисходная матрица:')
    for row in matrix:
        print(row)

    for i in range(n):
        min_val = min(matrix[i])
        min_idx = matrix[i].index(min_val)

        if min_val % 2 == 0:
            matrix[i][min_idx] = 0
        else:
            matrix[i][min_idx] = 1
    print('\nПосле замены минимальных элементов:')
    for row in matrix:
        print(row)
task_simple()
task2_simple()