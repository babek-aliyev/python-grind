import sys

sys.setrecursionlimit(1000000)

cache = {1: 1}

def cycle(n):
    if n in cache:
        return cache[n]

    if n % 2 == 0:
        cache[n] = 1 + cycle(n // 2)
    else:
        cache[n] = 1 + cycle(3 * n + 1)

    return cache[n]

for line in sys.stdin:
    if not line.strip():
        continue

    i, j = map(int, line.split())
    a, b = min(i, j), max(i, j)

    max_cycle = 0
    for x in range(a, b + 1):
        max_cycle = max(max_cycle, cycle(x))

    print(i, j, max_cycle)
