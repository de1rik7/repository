import random

def task1_simple():
    n, m = 4, 3
    matrix = [[random.randint(1, 10) for _ in range(m)] for _ in range(n)]

    print("Матрица:")
    for row in matrix:
        print(row)

    sums = [sum(row) for row in matrix]
    max_idx = sums.index(max(sums))
    min_idx = sums.index(min(sums))

    print(f"\nСтрока с наибольшей суммой: {matrix[max_idx]} (сумма: {sums[max_idx]})")
    print(f"Строка с наименьшей суммой: {matrix[min_idx]} (сумма: {sums[min_idx]})")
task1_simple()
