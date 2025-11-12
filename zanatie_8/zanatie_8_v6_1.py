def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input("Введите два числа: ").split())
nod = gcd(a, b)
nok = a * b // nod
print(f"НОД: {nod}, НОК: {nok}")