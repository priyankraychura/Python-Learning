class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
rec = Shape(5, 3)
print(rec.area())

c = Circle(5)
print(c.area())