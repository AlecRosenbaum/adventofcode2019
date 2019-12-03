"""
Day 2 challenge
"""
from intcode import intcode


def solution_part_one(arg, noun=None, verb=None):
    program = list(map(int, arg.split(",")))
    return ",".join(map(str, intcode(program, noun=noun, verb=verb)))


def solution_part_two(arg, desired_output=None):
    program = list(map(int, arg.split(",")))
    for noun in range(99):
        for verb in range(99):
            result = intcode(program.copy(), noun=noun, verb=verb)
            if result[0] == desired_output:
                return 100 * noun + verb


if __name__ == "__main__":
    with open("input.txt", "r") as fin:
        problem_input = fin.read()
    print(solution_part_one(problem_input, noun=12, verb=2))
    print(solution_part_two(problem_input, desired_output=19690720))
