import pytest

from solution import solution_part_one, solution_part_two


@pytest.mark.parametrize(
    "x,expected", [("12", 2), ("14", 2), ("1969", 654), ("100756", 33583)]
)
def test_solution_part_one(x, expected):
    assert expected == solution_part_one(x)


@pytest.mark.parametrize("x,expected", [("14", 2), ("1969", 966), ("100756", 50346)])
def test_solution_part_one(x, expected):
    assert expected == solution_part_two(x)
