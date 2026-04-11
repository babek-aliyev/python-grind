m, n = map(int, input().split())

is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

i = 2
while i * i <= n:
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
    i += 1

found = False

for x in range(m, n + 1):
    if is_prime[x]:
        print(x)
        found = True

if not found:
    print("Absent")
