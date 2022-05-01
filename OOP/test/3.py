class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        print(3.14 * self.radius ** 2)
    def get_perimeter(self):
        print(2 * 3.14 * self.radius)

circle1 = Circle(6)
circle1.get_area()
circle1.get_perimeter()
            