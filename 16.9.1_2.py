import math


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def circle_area(self):
        return math.pi*self.radius*self.radius


c = Circle(10, 10, 20)
print(c.circle_area())


def get_circle(x, y, radius):
    return "Circle({}, {}, {})".format(x, y, radius)


print(get_circle(10, 10, 10))