import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import Circle, Rectangle, Square, Triangle

def test_figure_positive(figures_date):
    figure = figures_date["figure"]
    expect_area = figures_date["expect_area"]
    expect_perimeter = figures_date["expect_perimeter"]
    sides = figures_date["sides"]

    if figure == "circle" :
        c = Circle(sides)
        assert c.get_area() == pytest.approx(expect_area) , (f"Вычисляемая площадь {c.get_area()} не равна тестовой {expect_area}")
        assert c.get_perimeter() == pytest.approx(expect_perimeter) , (f"Вычисляемый периметр {c.get_perimeter()} не равен тестовому {expect_perimeter}")

    elif figure == "triangle":
        t = Triangle(*sides)
        assert t.get_area() == pytest.approx(expect_area) , (f"Вычисляемая площадь {t.get_area()} не равна тестовой {expect_area}")
        assert t.get_perimeter() == pytest.approx(expect_perimeter) , (f"Вычисляемый периметр {t.get_perimeter()} не равен тестовому {expect_perimeter}")

    elif figure == "rectangle":
        r = Rectangle(*sides)
        assert r.get_area() == pytest.approx(expect_area) , (f"Вычисляемая площадь {r.get_area()} не равна тестовой {expect_area}")
        assert r.get_perimeter() == pytest.approx(expect_perimeter) , (f"Вычисляемый периметр {r.get_perimeter()} не равен тестовому {expect_perimeter}")

    elif figure == "square":
        s = Square(sides)
        assert s.get_area() == pytest.approx(expect_area) , (f"Вычисляемая площадь {s.get_area()} не равна тестовой {expect_area}")
        assert s.get_perimeter() == pytest.approx(expect_perimeter) , (f"Вычисляемый периметр {s.get_perimeter()} не равен тестовому {expect_perimeter}")

    else:
       raise ValueError(f"Тип {figure} не находится в перечне доступных для вычисления!")



