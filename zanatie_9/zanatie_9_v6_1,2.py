import random
def task1_simple():
    N = 4
    matrix = [[random.randint(1, 20) for _ in range(N)] for _ in range(N)]

    print('Матрица')
    for row in matrix:
        print(row)

    print('\nМаксимумы в строках:')
    for i in range(N):
        print(f"Строка {i}: {max(matrix[i])}")

    print('\nМинимумы с столбцах:')
    for j in range(N):
        col = [matrix[i][j] for i in range(N)]
        print(f'Столбец {j}: {min(col)}')
task1_simple()

def task2_simple():
    N = 5
    center = N // 2
    numders = random.sample(range(1, 100), N*N)
    matrix = [numders[i*N:(i+1)*N] for i in range(N)]

    print("\nИсходная матрица:")
    for row in matrix:
        print(row)

    max_val = matrix[0][0]
    max_pos = (0, 0)

    for i in range(N):
        if matrix[i][i] > max_val:
            max_val = matrix[i][i]
            max_pos = (i, i)
        j = N - 1 - i
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            max_pos = (i, j)

        print(f'\nМаксимальный на диагоналях: A[{max_pos[0]},{max_pos[1]}] = {max_val}')
        print(f'Центральный элемент: A[{center},{center}] = {matrix[center][center]}')

        if max_pos != (center, center):
            matrix[center][center], matrix[max_pos[0]][max_pos[1]] = matrix[max_pos[0]][max_pos[1]], matrix[center][center]
            print('Выполнен обмен')

            print('\nПосле обмена:')
            for row in matrix:
                print(row)
task2_simple()