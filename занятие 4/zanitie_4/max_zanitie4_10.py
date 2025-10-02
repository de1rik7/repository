N = int(input())
K = int(input())
if K == 1:
    a, b = 0, 1
elif K == 2:
    a, b = 1, 1
else:
    a, b = 1, 1
    for i in range(3, K + 1):
        a, b = b, a + b

total = b
for i in range(1, N):
    a, b = b, a + b
    total += b
print(total)