from rectangle import Rectangle
from triangle import Triangle
from square import Square
from circle import Circle

if __name__ == "__main__":
    t = Triangle(3, 3, 3)
    r = Rectangle(2, 3, 2, 3)
    s = Square(2)
    c = Circle(2)
    a = 2
    print(s.get_perimeter())