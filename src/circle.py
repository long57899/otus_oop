from figure import Figure


class Circle(Figure):
    pi = 3.14

    def __init__(self, *args):
        super().__init__(*args)
        self.validate_circle()

    def validate_circle(self):
        if len(self.lines) != 1:
            raise ValueError("Для вычисления нужен только радиус!")

    def get_area(self):
        return self.pi * (self.lines[0] ** 2)

    def get_perimeter(self):
        return 2 * self.pi * self.lines[0]
