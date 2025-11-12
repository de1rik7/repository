import math
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

triangles = [tuple(map(float, input(f"Катеты треугольника {i+1}: ").split())) for i in range(2)]
hypotenuses = [hypotenuse(*t) for t in triangles]

for i, h in enumerate(hypotenuses, 1):
    print(f"Гипотенуза {i}: {h:.2f}")

if hypotenuses[0] > hypotenuses[1]:
    print("Первая гипотенуза больше")
else:
    print("Вторая гипотенуза больше")