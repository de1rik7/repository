def is_valid(num):
    digits = set(map(int, str(num)))
    return all(d != 0 and num % d == 0 for d in digits)

n = int(input("Введите n: "))
result = [i for i in range(1, n + 1) if is_valid(i)]
print("Найденные числа:", *result)