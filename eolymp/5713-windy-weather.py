n = int(input())

arr = list(map(int, input().split()))
minim = arr[0]
maxim = arr[0]

for i in arr:
    if i>maxim:
        maxim=i
    if i<minim:
        minim=i

print(maxim-minim)
