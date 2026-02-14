a = int(input())

arr = list(map(int, input().split()))
mn = 999999
for i in arr:
    if mn>i:
        mn=i

print(mn)
