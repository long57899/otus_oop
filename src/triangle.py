from figure import Figure


class Triangle(Figure):
    def __init__(self, *args):
        super().__init__(*args)
        self.validate_triangle()

    def validate_triangle(self):
        if len(self.lines) != 3:
            raise ValueError("Для вычисления должно быть указано только 3 стороны!")
        elif self.lines[-1]>=(self.lines[0]+self.lines[1]):
            raise ValueError("Такого треугольника не существует!") 
            

    def get_area(self):
        a, b, c = self.lines
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def get_perimeter(self):
        perimeter = 0
        for line in self.lines:
            perimeter += line
        return perimeter
