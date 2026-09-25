import math

class Triangle:
    def __init__(self, a, b, c):
        self.name = "Trójkąt"
        if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Niepoprawne wartości boków trójkąta")
        self.a = a
        self.b = b
        self.c = c

    def count_surface_area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def count_perimeter(self):
        return self.a + self.b + self.c

    def display_name(self):
        print(f"Nazwa figury: {self.name}")


class Rectangle:
    def __init__(self, a, b):
        self.name = "Prostokąt"
        if a <= 0 or b <= 0:
            raise ValueError("Niepoprawne wartości boków prostokąta")
        self.a = a
        self.b = b

    def count_surface_area(self):
        return self.a * self.b

    def count_perimeter(self):
        return 2 * (self.a + self.b)

    def display_name(self):
        print(f"Nazwa figury: {self.name}")


class Circle:
    def __init__(self, r):
        self.name = "Koło"
        if r <= 0:
            raise ValueError("Promień koła musi być większy od zera")
        self.r = r

    def count_surface_area(self):
        return math.pi * self.r ** 2

    def count_perimeter(self):
        return 2 * math.pi * self.r

    def display_name(self):
        print(f"Nazwa figury: {self.name}")


try:
    triangle = Triangle(3, 4, 5)
    triangle.display_name()
    print("Pole trójkąta:", triangle.count_surface_area())
    print("Obwód trójkąta:", triangle.count_perimeter())
except ValueError as e:
    print(e)

try:
    rectangle = Rectangle(4, 6)
    rectangle.display_name()
    print("Pole prostokąta:", rectangle.count_surface_area())
    print("Obwód prostokąta:", rectangle.count_perimeter())
except ValueError as e:
    print(e)

try:
    circle = Circle(5)
    circle.display_name()
    print("Pole koła:", circle.count_surface_area())
    print("Obwód koła:", circle.count_perimeter())
except ValueError as e:
    print(e)
