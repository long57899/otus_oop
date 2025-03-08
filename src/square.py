from figure import Figure


class Square(Figure):
    def __init__(self, *args):
        super().__init__(*args)
        self.validate_square()

    def validate_square(self):
        if len(self.lines) not in (4, 2, 1):
            raise ValueError("Для вычисления сторон должно быть 4, 2 или 1!")
        elif len(self.lines) == 4:
            a, b, c, d = self.lines
            if not (a == b == c == d):
                raise ValueError("Все стороны квадрата должны быть равны!")
        elif len(self.lines) == 2:
            if not (self.lines[0] == self.lines[-1]):
                raise ValueError("Все стороны квадрата должны быть равны!")

    def get_area(self):
        return self.lines[0] ** 2
        

    def get_perimeter(self):
        return self.lines[0] * 4
