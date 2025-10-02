prev = int(input())
count = 0
num = int(input())

while num != 0:
    if num > prev:
        count += 1
    prev = num
    num = int(input())

print(count)