import math
n = int(input())
x = math.ceil(math.sqrt(n))
divisor=n
for i in range(2, x):
    if n%i==0:
        divisor=i
        break

print(divisor)
