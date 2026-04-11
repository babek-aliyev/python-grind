import math

n = int(input())

if n < 2:
    print("No")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break

    print("Yes" if is_prime else "No")
