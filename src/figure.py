class Figure:
    def __init__(self, *args):
        for line in args:
            if not isinstance(line, (int, float)):
                raise TypeError("Все стороны должны быть числами.")
            if line <= 0:
                raise ValueError("Стороны должны быть положительными числами!")

        self.lines = sorted(args)

    def add_area(self, figure):
        if not hasattr(figure, "get_area"):
            raise ValueError(f"\"{figure}' - не является наследником Figure!")
        else:
            return figure.get_area() + self.get_area()
