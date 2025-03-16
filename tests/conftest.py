import pytest

@pytest.fixture(params=[
    {"sides":2,
    "expect_area":12.56,
    "expect_perimeter":12.56},

    {"sides":3,
    "expect_area":28.26,
    "expect_perimeter":18.84},

], ids=[
    "Tests area and perimeter of circle with radius = 2",
    "Tests area and perimeter of circle with radius = 3",
       ] , scope="module")
def circle_date(request):
    return request.param


@pytest.fixture(params=[
    {"sides":(3,3,3),
    "expect_area":3.897,
    "expect_perimeter":9},

    {"sides":(4,4,4),
    "expect_area":6.928,
    "expect_perimeter":12},

], ids=[
    "Tests area and perimeter of triangle with sides = 3,3,3",
    "Tests area and perimeter of triangle with sides = 4,4,4",
    ] , scope="module")
def triangle_date(request):
    return request.param


@pytest.fixture(params=[
    {"sides":(2, 3, 2, 3),
    "expect_area":6,
    "expect_perimeter":10},

    {"sides":(5,6),
    "expect_area":30,
    "expect_perimeter":22},

], ids=[
    "Tests area and perimeter of rectangle with radius = 2, 3, 2, 3",
    "Tests area and perimeter of rectangle with radius = 5,6",
       ] , scope="module")
def rectangle_date(request):
    return request.param


@pytest.fixture(params=[
    {"sides":2,
    "expect_area":4,
    "expect_perimeter":8},

    {"sides":4,
    "expect_area":16,
    "expect_perimeter":16},

], ids=[
    "Tests area and perimeter of square with sides = 2",
    "Tests area and perimeter of square with sides = 4",
       ] , scope="module")
def square_date(request):
    return request.param