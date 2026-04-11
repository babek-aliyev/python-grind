n, m = map(int, input().split())

result = 0
mod = m
p = pow  # local reference (faster)

for i in range(1, n + 1):
    result += p(i, i, mod)
    if result >= mod:
        result %= mod

print(result % mod)
