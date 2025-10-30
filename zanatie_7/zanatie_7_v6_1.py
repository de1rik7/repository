arr = [int(input(f"Введите элемент {i+1}: ")) for i in range(10)]

average = sum(arr) / 10
max_element = max(arr)

count_less_max = 0
count_greater_avg = 0

for num in arr:
    if num < max_element:
        count_less_max += 1
    if num > average:
        count_greater_avg += 1

print("Массив:", arr)
print(f"Среднее арифметическое: {average}")
print(f"Количество элементов меньше максимального: {count_less_max}")
print(f"Количество элементов больше среднего: {count_greater_avg}")