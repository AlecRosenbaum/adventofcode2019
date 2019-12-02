"""
Day 1 challenge
"""
import math


def get_fuel(mass):
    return max(0, math.floor(mass / 3) - 2)


def solution_part_one(arg):
    return sum([get_fuel(int(mass)) for mass in arg.split("\n") if mass])


def solution_part_two(arg):
    tot = 0
    for mass in arg.split("\n"):
        if not mass:
            continue
        step = int(mass)
        while step == int(mass) or step > 0:
            step = get_fuel(step)
            tot += step
    return tot


if __name__ == "__main__":
    with open("input.txt", "r") as fin:
        problem_input = fin.read()
    print(solution_part_one(problem_input))
    print(solution_part_two(problem_input))
