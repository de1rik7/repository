n = int(input("Введите количество элементов: "))
arr = [int(input(f"Введите элемент {i+1}: ")) for i in range(n)]

sum_even = 0
product_odd = 1

for i in range(n):
    if i % 2 == 0:
        sum_even += arr[i]
    else:
        product_odd *= arr[i]

print("Массив:", arr)
print("Сумма элементов с четными индексами:", sum_even)
print("Произведение элементов с нечетными индексами:", product_odd)