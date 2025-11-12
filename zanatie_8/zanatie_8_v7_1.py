import math
def right_triangle_area(a, b):
    return 0.5 * a * b

def rectangle_area(a, b):
    return a * b

x, y, z, t = map(float, input("Введите X, Y, Z, T: ").split())
area_triangle = right_triangle_area(x, y)
hypo = math.sqrt(x**2 + y**2)
area_rect = rectangle_area(z, t)
print(f"Площадь четырёхугольника: {area_triangle + area_rect:.2f}")