arr = [int(input(f"Введите элемент {i+1}: ")) for i in range(10)]

sum_greater_5 = sum(num for num in arr if num > 5)

print("Массив:", arr)
print("Сумма чисел больше 5:", sum_greater_5)