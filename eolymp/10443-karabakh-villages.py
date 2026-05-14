n, q = map(int, input().split())
arr = list(map(int, input().split()))

freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1

for _ in range(q):
    x = int(input())
    print(freq.get(x, 0))
