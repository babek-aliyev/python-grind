arr = list(map(int, str(input())))
max = arr[0]

for i in arr:
    if i>max:
        max=i

print(max)
