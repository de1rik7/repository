n = int(input("Введите количество элементов массива: "))
arr = [int(input(f"Введите элемент {i+1}: ")) for i in range(n)]

min_index = arr.index(min(arr))
print("Индекс минимального элемента:", min_index)