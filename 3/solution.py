"""
Day 3 challenge
"""

from collections import defaultdict


def solution_part_one(arg):
    wires = arg.split("\n")

    dirs = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1),
    }
    board = defaultdict(set)
    for idx, wire in enumerate(wires):
        if not wire:
            continue
        position = (0, 0)
        for move in wire.split(","):
            direction, n_str = move[0], move[1:]
            for _ in range(int(n_str)):
                dx, dy = dirs[direction]
                position = (position[0] + dx, position[1] + dy)
                board[position].add(idx)

    return min(
        [abs(pos[0]) + abs(pos[1]) for pos, wires in board.items() if len(wires) > 1]
    )


def solution_part_two(arg):
    wires = arg.split("\n")

    dirs = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1),
    }
    board = defaultdict(dict)
    for idx, wire in enumerate(wires):
        if not wire:
            continue
        position = (0, 0)
        moves = 0
        for move in wire.split(","):
            direction, n_str = move[0], move[1:]
            for _ in range(int(n_str)):
                moves += 1
                dx, dy = dirs[direction]
                position = (position[0] + dx, position[1] + dy)
                board[position].setdefault(idx, moves)

    print(
        [list(wires.values()) for pos, wires in board.items() if len(wires.keys()) > 1]
    )
    return min(
        [sum(wires.values()) for pos, wires in board.items() if len(wires.keys()) > 1]
    )


if __name__ == "__main__":
    with open("input.txt", "r") as fin:
        problem_input = fin.read()
    print(solution_part_one(problem_input))
    print(solution_part_two(problem_input))
