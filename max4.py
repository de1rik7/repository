def calculate_lace_lenght(a, b, l, N):
     horizontal = (N - 1) * b * 2
     vertical = (2 * N - 1) * a 
     total = horizontal + vertical + 2 * 1
     return total
a = int(input())
b = int(input())
l = int(input())
N = int(input())
result = calculate_lace_lenght(a, b, l, N)
print(result)
