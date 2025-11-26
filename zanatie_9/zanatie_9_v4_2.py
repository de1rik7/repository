import random

def task2_simple():
    N = 4
    matrix = [[random.randint(-5, 5) for _ in range(N)] for _ in range(N)]

    print("\nИсходная матрица:")
    for row in matrix:
        print(row)
    for i in range(N):
        for j in range(N):
            if matrix[i][j] < 0:
                matrix[i][j] = 0
            elif matrix[i][j] > 0:
                matrix[i][j] = 1

    print("\nПосле замены (0 и 1):")
    for row in matrix:
        print(row)

    print("\nНижняя треугольная матрица:")
    for i in range(N):
        for j in range(N):
            if i >= j:
                print(matrix[i][j], end=" ")
            else:
                print(" ", end=" ")
        print()
task2_simple()
