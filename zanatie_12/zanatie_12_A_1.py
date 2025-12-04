def p(x, n):
    return 1 if n == 0 else x * p(x, n-1)

def f(n):
    return 1 if n <= 1 else n * f(n-1)

x, n = map(int, input("Введите X и N: ").split())
print(f"{p(x, n)/f(n):.4f}")