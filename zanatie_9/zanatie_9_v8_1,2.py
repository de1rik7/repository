import random
def task1_simple():
    n = 4
    k = 1
    matrix = [[random.randint(1, 5) for _ in range(n)] for _ in range(n)]

    print("Исходная матрица:")
    for row in matrix:
        print(row)

    diagonal = matrix[k][k]
    if diagonal == 0:
        print("Ошибка: деление на ноль")
        return

    for j in range(n):
        matrix[k][j] = round(matrix[k][j] / diagonal, 2)

    print(f"\nПосле деления строки {k} на диагональный элемент {diagonal}:")
    for row in matrix:
        print(row)


def task2_simple():
    n = 3
    matrix = [[random.randint(1, 9) for _ in range(n)] for _ in range(n)]

    print("\nИсходная матрица:")
    for row in matrix:
        print(row)

    transposed = []
    for i in range(n):
        new_row = [matrix[j][i] for j in range(n)]
        transposed.append(new_row)

    print("\nТранспонированная матрица:")
    for row in transposed:
        print(row)
task1_simple()
task2_simple()