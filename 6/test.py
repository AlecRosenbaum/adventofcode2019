import pytest

from solution import solution_part_one, solution_part_two

PART_ONE_SAMPLE_INPUT = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""


@pytest.mark.parametrize(
    "x,expected",
    [
        (PART_ONE_SAMPLE_INPUT, 42),
        ("COM)B", 1),
        ("COM)B\nB)C", 3),
        ("COM)B\nB)C\nB)D\nD)E", 8),
    ],
)
def test_solution_part_one(x, expected):
    assert expected == solution_part_one(x)


PART_TWO_SAMPLE_INPUT = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""


@pytest.mark.parametrize("x,expected", [(PART_TWO_SAMPLE_INPUT, 4)])
def test_solution_part_one(x, expected):
    assert expected == solution_part_two(x)
