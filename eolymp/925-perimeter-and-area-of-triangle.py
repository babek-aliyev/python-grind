import math

x1, y1, x2, y2, x3, y3 = map(float, input().split())

a = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
b = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
c = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)

perimeter = a + b + c

s = perimeter / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"{perimeter:.4f} {area:.4f}")
