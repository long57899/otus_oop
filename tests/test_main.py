import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import Circle, Rectangle, Square, Triangle

def test_circle_positive(circle_date):
    expect_area = circle_date["expect_area"]
    expect_perimeter = circle_date["expect_perimeter"]
    sides = circle_date["sides"]
    
    c = Circle(sides)
    assert c.get_area() == pytest.approx(expect_area) , (f"Вычисляемая площадь {c.get_area()} не равна тестовой {expect_area}")
    assert c.get_perimeter() == pytest.approx(expect_perimeter) , (f"Вычисляемый периметр {c.get_perimeter()} не равен тестовому {expect_perimeter}")


def test_triangle_positive(triangle_date):
    expect_area = triangle_date["expect_area"]
    expect_perimeter = triangle_date["expect_perimeter"]
    sides = triangle_date["sides"]        

    t = Triangle(*sides)
    assert t.get_area() == pytest.approx(expect_area) , (f"Вычисляемая площадь {t.get_area()} не равна тестовой {expect_area}")
    assert t.get_perimeter() == pytest.approx(expect_perimeter) , (f"Вычисляемый периметр {t.get_perimeter()} не равен тестовому {expect_perimeter}")

def test_rectangle_positive(rectangle_date):
    expect_area = rectangle_date["expect_area"]
    expect_perimeter = rectangle_date["expect_perimeter"]
    sides = rectangle_date["sides"]

    r = Rectangle(*sides)
    assert r.get_area() == pytest.approx(expect_area) , (f"Вычисляемая площадь {r.get_area()} не равна тестовой {expect_area}")
    assert r.get_perimeter() == pytest.approx(expect_perimeter) , (f"Вычисляемый периметр {r.get_perimeter()} не равен тестовому {expect_perimeter}")

def test_square_positive(square_date):
    expect_area = square_date["expect_area"]
    expect_perimeter = square_date["expect_perimeter"]
    sides = square_date["sides"]

    s = Square(sides)
    assert s.get_area() == pytest.approx(expect_area) , (f"Вычисляемая площадь {s.get_area()} не равна тестовой {expect_area}")
    assert s.get_perimeter() == pytest.approx(expect_perimeter) , (f"Вычисляемый периметр {s.get_perimeter()} не равен тестовому {expect_perimeter}")
