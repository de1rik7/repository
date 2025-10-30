n = int(input("Введите количество элементов: "))
arr = [int(input(f"Введите элемент {i+1}: ")) for i in range(n)]

min_index = arr.index(min(arr))
max_index = arr.index(max(arr))

print("Исходный массив:", arr)
# Меняем местами min и max
arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
print("Массив после перестановки:", arr)