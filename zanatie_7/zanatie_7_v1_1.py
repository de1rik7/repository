n = int(input("Введите количество элементов массива: "))
arr = [int(input(f"Введите элемент {i+1}: ")) for i in range(n)]

max_element = max(arr)
print("Максимальный элемент:", max_element)
print("Массив в обратном порядке:", arr[::-1])