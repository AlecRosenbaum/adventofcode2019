import pytest

from solution import meets_criteria, solution_part_one, solution_part_two


@pytest.mark.parametrize(
    "x,expected", [("111111", True), ("223450", False), ("123789", False)]
)
def test_meets_criteria(x, expected):
    assert expected == meets_criteria(x, min_val=0, max_val=999999)


@pytest.mark.parametrize(
    "x,expected", [("112233", True), ("123444", False), ("111122", True)]
)
def test_solution_part_one(x, expected):
    assert expected == meets_criteria(x, min_val=0, max_val=999999, exact_double=True)
