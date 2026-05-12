class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def onLine(self, a, b, c):
        if self.x*a+self.y*b+c==0:
            print('YES')
        else:
            print('NO')

x,y,a,b,c = map(int, input().split())
p = Point(x,y)
p.onLine(a,b,c)
