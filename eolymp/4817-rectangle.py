import sys

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

for line in sys.stdin:
    x,y = map(int, line.split())
    r = Rectangle(x,y)
    print(2*(x+y), x*y)
