a, b = map(int, input().split())

arr = []

for i in range(a, b+1):
    nums = list(str(i))
    if len(set(nums))==4:
                arr.append(i)

for i in arr:
    print(i,end=" ")
