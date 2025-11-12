def swap_first_last(arr):
    arr[0], arr[-1] = arr[-1], arr[0]

m = int(input("Длина массива: "))
arr = list(map(int, input("Элементы массива: ").split()))
print("Исходный массив:", *arr)
swap_first_last(arr)
print("Изменённый массив:", *arr)