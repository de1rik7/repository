n = int(input("Введите количество элементов: "))
arr = [int(input(f"Введите элемент {i+1}: ")) for i in range(n)]

odd_numbers = [x for x in arr if x % 2 != 0]

if not odd_numbers:
    print("Нечетных чисел нет")
else:
    odd_numbers.sort(reverse=True)
    print("Нечетные числа в порядке убывания:", odd_numbers)