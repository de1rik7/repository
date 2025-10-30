arr = [int(input(f"Введите элемент {i+1}: ")) for i in range(10)]

unique_arr = []
for num in arr:
    if num not in unique_arr:
        unique_arr.append(num)

print("Исходный массив:", arr)
print("Массив без дубликатов:", unique_arr)