"""
Day N challenge
"""
from collections import defaultdict
from functools import reduce
from operator import __or__ as OR


def solution_part_one(arg):
    orbits = defaultdict(list)
    for a, b in [i.split(")") for i in arg.split("\n") if i]:
        orbits[a].append(b)

    def traverse(current, depth=0):
        return sum([traverse(i, depth=depth + 1) for i in orbits[current]] + [depth])

    return traverse("COM")


def solution_part_two(arg):
    orbits = defaultdict(list)
    for a, b in [i.split(")") for i in arg.split("\n") if i]:
        orbits[a].append(b)

    def path(from_, to_, curr_path=[]):
        if from_ == to_:
            return curr_path
        return reduce(lambda agg, x: agg or x, [path(from_=i, to_=to_, curr_path=curr_path + [from_]) for i in orbits[from_]], [])

    a = path("COM", "YOU")
    b = path("COM", "SAN")

    while a[0] == b[0]:
        a.pop(0)
        b.pop(0)

    return len(a) + len(b)



if __name__ == "__main__":
    with open("input.txt", "r") as fin:
        problem_input = fin.read()
    print(solution_part_one(problem_input))
    print(solution_part_two(problem_input))
