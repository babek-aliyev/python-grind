n, k = map(int, input().split())
arr = list(map(int, input().split()))

s = set(arr)

count = 0
for x in arr:
    if x + k in s:
        count += 1

print(count)
