a, b, c, d = map(int, input().split())

if a > b:
    a, b = b, a
if c > d:
    c, d = d, c

s = set()

for i in range(a, b + 1):
    for j in range(c, d + 1):
        s.add(i * j)

print(len(s))
