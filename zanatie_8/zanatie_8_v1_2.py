arrays = [
    list(map(int, input(f"Введите массив {i+1} (через пробел): ").split()))
    for i in range(3)
]

for i, arr in enumerate(arrays, 1):
    total = sum(arr)
    average = total / len(arr)
    print(f"Массив {i}: Сумма = {total}, Среднее = {average:.2f}")