import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @staticmethod
    def distance(p1, p2):
        d = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 )
        return d
x = Point(0, 0)
y = Point(0, 5)                             
print(Point.distance(x, y))                 