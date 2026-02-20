n = int(input())
arr = [i for i in range(1, n+1)]
for i in range(1, n+1):
    for j in arr:
        print(f"{i*j:2}", end=" ")
    print()


