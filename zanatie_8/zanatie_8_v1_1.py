def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

print("Выберите фигуру: 1 - прямоугольник, 2 - треугольник")
choice = int(input())

if choice == 1:
    a = float(input("Длина: "))
    b = float(input("Ширина: "))
    print(f"Площадь прямоугольника: {rectangle_area(a, b)}")
elif choice == 2:
    base = float(input("Основание: "))
    h = float(input("Высота: "))
    print(f"Площадь треугольника: {triangle_area(base, h)}")