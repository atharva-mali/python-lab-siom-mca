# __str__ method allows class to comvert itself into string

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(atharva):
        return "(" + str(atharva.x) + ", " + str(atharva.y) + ")"
    
p=Point(2,5)
p.__str__()
print(p)
        