lst = list(map(int, input().split()))
mx = lst[0]

for i in lst:
    if i>mx:
        mx=i

print(mx)

