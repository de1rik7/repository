n = int(input("Введите количество элементов в списке: "))

arr = []
for i in range(n):
    element = int(input(f"Введите элемент {i+1}: "))
    arr.append(element)

total_sum = sum(arr)
product = 1
for num in arr:
    product *= num

print("\nИсходный список:", arr)
print(f"Сумма элементов: {total_sum}")
print(f"Произведение элементов: {product}")