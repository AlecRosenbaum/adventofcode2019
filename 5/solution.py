"""
Day 2 challenge
"""
from intcode import intcode


def solution_part_one(arg):
    state = intcode(arg, input_=[1])
    return ",".join(map(str, state.output))


def solution_part_two(arg):
    state = intcode(arg, input_=[5])
    return ",".join(map(str, state.output))


if __name__ == "__main__":
    with open("input.txt", "r") as fin:
        problem_input = fin.read()
    print(solution_part_one(problem_input))
    print(solution_part_two(problem_input))
