class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def onCircle(self, xa, ya):
        if ((self.x-xa)**2+(self.y-ya)**2)<=(self.r)**2:
            print('YES')
        else:
            print('NO')

x,y,r = map(int, input().split())
xa, ya = map(int, input().split())
c = Circle(x,y,r)
c.onCircle(xa,ya)

