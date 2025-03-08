from figure import Figure


class Rectangle(Figure):
    def __init__(self, *args):
        super().__init__(*args)
        self.validate_rectangle()

    def validate_rectangle(self):
        if len(self.lines) not in (2, 4):
            raise ValueError("Для вычисления сторон должно быть 4 или 2!")
        elif len(self.lines) == 4:
            a, b, c, d = self.lines
            if not (a == b and c == d):
                raise ValueError(
                    "Стороны должны быть попарно равны!"
                )

    def get_area(self):
        return self.lines[0] * self.lines[-1]

    def get_perimeter(self):
        return (self.lines[0] * 2) + (self.lines[-1] * 2)
