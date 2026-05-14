import math

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def angle(self, p):
        dotProduct = self.x*p.x+self.y*p.y
        selfMagnitude = math.sqrt(self.x**2+self.y**2)
        otherMagnitude = math.sqrt(p.x**2+p.y**2)
        value = dotProduct/(selfMagnitude*otherMagnitude)
        angle = math.acos(value)
        return angle

x1,y1,x2,y2 = map(int, input().split())
p1 = Point(x1,y1)
p2 = Point(x2,y2)
print(f"{p1.angle(p2):.5f}") 
