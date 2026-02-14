import math
n, m, k = map(int, input().split())

boys = math.ceil(n/k)
girls = math.ceil(m/k)

print(boys+girls)
