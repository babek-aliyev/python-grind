import sys

n = int(input())

for i in sys.stdin:
    lst = list(map(int, i.split()))

st = set(lst)
print(sum(st)/len(st))
