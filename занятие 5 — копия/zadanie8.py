current = int(input())
max_count = 1
current_count = 1
prev = current

while current != 0:
    current = int(input())
    if current == 0:
        break
    if current == prev:
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 1
    prev = current

print(max_count)