def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b, c, d = map(int, input("Введите A, B, C, D: ").split())
num = a * d
den = b * c
divisor = gcd(num, den)
print(f"Результат: {num // divisor}/{den // divisor}")