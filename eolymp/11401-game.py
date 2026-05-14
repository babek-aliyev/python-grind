n = int(input())
arr = list(map(int, input().split()))

s = set()

for x in arr:
    if x in s:
        s.remove(x)
    else:
        s.add(x)

print(len(s))
