from functools import lru_cache
import math

@lru_cache(maxsize=None)
def f(n):
    if n<=2:
        return 1
    elif n%2==1:
        return f(math.floor((6*n)/7)) + f(math.floor((2*n)/3))
    else:
        return f(n-1)+f(n-3)


n = int(input())
print(f(n)%2**32)
