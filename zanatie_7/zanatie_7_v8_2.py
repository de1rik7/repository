n = int(input("\nВведите количество элементов в массиве: "))

arr = []
for i in range(n):
    element = float(input(f"Введите элемент {i+1}: "))
    arr.append(element)

print("Исходный массив:", arr)

average = sum(arr) / n
print(f"Среднее арифметическое всех элементов: {average}")


for i in range(n):
    if arr[i] == 0:
        arr[i] = average

print("Измененный массив:", arr)