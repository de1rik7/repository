n = int(input("Введите количество элементов массива:"))
arr = [int(input(f"ведите элемент {i+1}: ")) for i in range(n)]

positive = [x for x in arr if x > 0]
other = [x for x in arr if x <= 0]

print('Положительные элементы: ', positive)
print('Остальные элементы: ', other)