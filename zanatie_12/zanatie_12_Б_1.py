def find_max():
    x = int(input())
    if x == 0:
        return 0
    max_rest = find_max()
    return x if x > max_rest else max_rest

print("Введите последовательность (окончите 0):")
print("Максимум:", find_max())