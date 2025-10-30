n = int(input("Введите количество элементов: "))
arr = [int(input(f"Введите элемент {i+1}: ")) for i in range(n)]

max_element = max(arr)
max_index = arr.index(max_element)

print("Массив:", arr)
print(f"Максимальный элемент: {max_element}, его индекс: {max_index}")