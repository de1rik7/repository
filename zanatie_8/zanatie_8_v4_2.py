def is_inside(circle, point):
    return (point[0] - circle[0])**2 + (point[1] - circle[1])**2 <= circle[2]**2

circle_data = tuple(map(float, input("Введите a, b, R: ").split()))
points = [
    tuple(map(float, input(f"Координаты точки {name}: ").split()))
    for name in ['P', 'F', 'L']
]

count = sum(is_inside(circle_data, p) for p in points)
print(f"Точек внутри окружности: {count}")
