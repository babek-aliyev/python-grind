n = int(input())
res = set()
for _ in range(n):
    lst = list(map(int, input().split()))
    st = set(lst[1:])
    res = res.union(st)

print(len(res))
