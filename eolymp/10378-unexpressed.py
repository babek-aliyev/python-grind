n = int(input())

s = set()

a = 2
while a * a <= n:
    val = a * a
    while val <= n:
        s.add(val)
        val *= a
    a += 1

print(n - len(s))
