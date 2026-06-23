class Shape:
    def __init__(self):
        pass
    def area():
        pass
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def __str__(self):
        return f"Circle(radius={self.radius})"
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width * self.height
    def __str__(self):
        return f"Rectangle(width={self.width},height={self.height})"
class Triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5 * self.base * self.height
    def __str__(self):
        return f"Triangle(base={self.base},height={self.height}) "

Shapes=[Circle(2),Rectangle(4,6),Triangle(5,6)]
for shape in Shapes:
    print(shape)
    print("Area:",shape.area())