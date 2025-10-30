n = int(input("Введите длину массива: "))
D = [int(input(f"Введите элемент {i+1}: ")) for i in range(n)]

sum_odd = 0
for i in range(1, n, 2):  # Индексы 1, 3, 5...
    sum_odd += D[i]

print("Массив D:", D)
print("Сумма элементов с нечетными индексами:", sum_odd)