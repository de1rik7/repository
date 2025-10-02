N = int(input())
power = 1
exponent = 0
while power * 2 <= N:
    power *= 2
    exponent += 1
print(exponent, power)