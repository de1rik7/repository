total = 0
count = 0
num = int(input())

while num != 0:
    total += num
    count += 1
    num = int(input())

if count > 0:
    print(total / count)
else:
    print(0)