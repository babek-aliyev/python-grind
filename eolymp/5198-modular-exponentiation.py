def mod(x,n,m):
    if n==0:
        return 1
    if n%2==0:
        return (mod(x, n//2, m)*mod(x, n//2, m))%m
    else:
        return (x*mod(x, n-1, m))%m

x,n,m=map(int, input().split())
print(mod(x,n,m))
