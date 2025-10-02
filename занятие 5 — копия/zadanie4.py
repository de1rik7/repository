x = float(input())
y = float(input())
day = 1
distance = x

while distance < y:
    distance += distance * 0.1
    day += 1

print(day)