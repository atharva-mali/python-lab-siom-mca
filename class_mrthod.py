# Class Method

class Point:
    """This class defines a point in 2D space"""
    def __init__(self,x,y):
        """Post: returns a Point with the given x and y fields"""
        self.x=x
        self.y=y
    
    @classmethod
    def help(cls):
        for attr in cls.__dict__:
            print(str(attr) if x is not None else +":"+cls.__dict__[attr].__doc__)
            print(x)

x=Point(0,0)
x.help()    