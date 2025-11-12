import math
def triangle_area(a, h):
    return 0.5 * a * h

def hexagon_area(a):
    return 6 * triangle_area(a, a * math.sqrt(3) / 2)

side = float(input("Сторона шестиугольника: "))
print(f"Площадь шестиугольника: {hexagon_area(side):.2f}")