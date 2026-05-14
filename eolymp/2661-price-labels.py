n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

result = set(a) | set(b)

print(*sorted(result))
