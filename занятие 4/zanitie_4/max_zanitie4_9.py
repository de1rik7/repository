n = int(input())
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    a, b = 0, 1
    total = 1
    for i in range(2, n):
        a, b = b, a + b
        total += b
print(total)