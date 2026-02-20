n = int(input())
main = 0
second = 0
for i in range(n):
    matrix = list(map(int, input().split()))
    main+=matrix[i]
    second+=matrix[n-i-1]

print(main, second)
