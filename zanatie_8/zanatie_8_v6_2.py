import math
def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

a, b, c, d, diag = map(float, input("Введите 4 стороны и диагональ: ").split())
area1 = triangle_area(a, b, diag)
area2 = triangle_area(c, d, diag)
print(f"Площадь четырёхугольника: {area1 + area2:.2f}")