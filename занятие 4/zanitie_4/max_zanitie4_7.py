n = int(input())
total = 0
current_factorial = 1
for i in range(1, n+1):
    current_factorial *= i
    total += current_factorial
print(total)