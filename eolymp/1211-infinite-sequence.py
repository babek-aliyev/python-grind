import sys
sys.setrecursionlimit(10**7)

n, p, q = map(int, input().split())

memo = {0: 1}

def A(x):
    if x in memo:
        return memo[x]
    memo[x] = A(x // p) + A(x // q)
    return memo[x]

print(A(n))
