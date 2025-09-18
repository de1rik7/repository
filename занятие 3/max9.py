def can_break_cholate():
   n = int(input())
   m = int(input())
   k = int(input())
   if (k % n == 0 or k % m == 0) and k <= n * m:
     print("Да")
   else: 
     print("Нет")
can_break_cholate()
