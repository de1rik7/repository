def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b, c, d = map(int, input("Введите A, B, C, D: ").split())
num = a * d - b * c
den = b * d
divisor = gcd(abs(num), den)
print(f"Результат: {num // divisor}/{den // divisor}")