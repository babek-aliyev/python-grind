import math
x = float(input())
func = lambda x: x + math.sin(x)

print(f"{func(x):.4f}")
