import pytest

from solution import solution_part_one, solution_part_two


@pytest.mark.parametrize(
    "x,expected",
    [
        ("1,9,10,3,2,3,11,0,99,30,40,50", "3500,9,10,70,2,3,11,0,99,30,40,50"),
        ("1,0,0,0,99", "2,0,0,0,99"),
        ("2,3,0,3,99", "2,3,0,6,99"),
        ("2,4,4,5,99,0", "2,4,4,5,99,9801"),
        ("1,1,1,4,99,5,6,0,99", "30,1,1,4,2,5,6,0,99"),
    ],
)
def test_solution_part_one(x, expected):
    assert expected == solution_part_one(x)


# @pytest.mark.parametrize("x,expected", [("14", 2), ("1969", 966), ("100756", 50346)])
# def test_solution_part_one(x, expected):
#     assert expected == solution_part_two(x)
