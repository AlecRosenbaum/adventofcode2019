"""
Day 4 challenge
"""

PUZZLE_INPUT = (273025, 767253)


def meets_criteria(
    x, min_val=PUZZLE_INPUT[0], max_val=PUZZLE_INPUT[1], exact_double=False
):
    assert isinstance(x, str)
    assert 6 == len(x)
    assert min_val <= int(x) <= max_val, f"{x} not in range {min_val}-{max_val}"
    double = False
    prev = x[0]
    rep = [prev]
    for idx, digit in enumerate(x[1:]):
        if digit == rep[0]:
            rep.append(digit)
        if digit != rep[0] or idx == 4:
            double = double or (len(rep) == 2 or (not exact_double and len(rep) >= 2))
            rep = [digit]

        if int(digit) < int(prev):
            return False

        prev = digit

    return double


def solution_part_one():
    return sum(
        1
        for i in range(PUZZLE_INPUT[0] + 1, PUZZLE_INPUT[1] - 1)
        if meets_criteria(str(i))
    )


def solution_part_two():
    return sum(
        1
        for i in range(PUZZLE_INPUT[0] + 1, PUZZLE_INPUT[1] - 1)
        if meets_criteria(str(i), exact_double=True)
    )


if __name__ == "__main__":
    print(solution_part_one())
    print(solution_part_two())
