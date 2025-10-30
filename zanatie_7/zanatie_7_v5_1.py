arr = [int(input(f"Введите элемент {i+1}: ")) for i in range(10)]

print("Пары отрицательных чисел:")
for i in range(9):
    if arr[i] < 0 and arr[i+1] < 0:
        print(f"({arr[i]}, {arr[i+1]})")