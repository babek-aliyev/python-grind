a = int(input())

arr = list(map(int, input().split()))
mn = arr[0]
for i in arr:
    if mn>i:
        mn=i

print(mn)
