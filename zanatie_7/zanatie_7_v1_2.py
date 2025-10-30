n = int(input("Введите количество элементов массива: "))
arr = [float(input(f"Введите элемент {i+1}: ")) for i in range(n)]

average = sum(arr) / n
for i in range(n):
    if arr[i] == 0:
        arr[i] = average

print("Измененный массив:", arr)