A = int(input("A: "))
B = int(input("B: "))
start = A if A % 2 != 0 else A -1
for i in range(start, B - 1, -2):
     print(i)
