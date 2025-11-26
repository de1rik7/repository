import random
def task2_simple():
    N, M = 4, 6
    B = [[random.randint(-10, 10) for _ in range(M)] for _ in range(N)]

    print("\nИсходная матрица B:")
    for row in B:
        print(row)

    for i in range(N):
        row = B[i]
        min_idx = row.index(min(row))
        max_idx = row.index(max(row))

        row[min_idx], row[-1] = row[-1], row[min_idx]
        row[max_idx], row[0] = row[0], row[max_idx]

    print("\nМатрица B после преобразований:")
    for row in B:
        print(row)
task2_simple()
