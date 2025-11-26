N = 3
A = [[1, -2, 3],
     [4, 5, -6],
     [7, 8, 9]]

count = 0
total = 0
for i in range(N):
    for j in range(i + 1, N):
        if A[i][j] > 0:
            count += 1
            total += A[i][j]

print(f"Сумма: {total}, Количество: {count}")