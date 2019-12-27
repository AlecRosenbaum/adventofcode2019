"""
Day 7 challenge
"""
from itertools import permutations

from intcode import intcode, ProgramState, Stop, InputRequired


def calc_amplification(program, phase_sequence):
    state = intcode(program, input_=[phase_sequence[0], 0])
    for phase in phase_sequence[1:]:
        assert 1 == len(state.output)
        state = intcode(program, input_=[phase, state.output[0]])

    return state


def solution_part_one(arg):
    amplifications = {}
    for permutation in permutations(range(5)):
        amplifications[permutation] = calc_amplification(arg, permutation).output[0]
    return max(amplifications.values())


def calc_amplification_feedback(program, phase_sequence):
    states = []
    for phase in phase_sequence:
        state = ProgramState.from_csv(program)
        state.input_ = [phase]
        states.append(state)
    states[0].input_.append(0)
    stopped = 0
    state_cnt = 0
    while stopped < len(states):
        curr_state = states[state_cnt % len(states)]
        if state_cnt and states[(state_cnt - 1) % len(states)].output:
            curr_state.input_.append(states[(state_cnt - 1) % len(states)].output.pop(0))
        try:
            while not curr_state.output:
                curr_state.step()
        except Stop:
            stopped += 1
        state_cnt += 1

    # output from last phase is copied to input after the last phase exists
    assert 1 == len(states[0].input_)
    return states[0].input_[0]


def solution_part_two(arg):
    amplifications = {}
    for permutation in permutations(range(5, 10)):
        amplifications[permutation] = calc_amplification_feedback(arg, permutation)
    return max(amplifications.values())


if __name__ == "__main__":
    with open("input.txt", "r") as fin:
        problem_input = fin.read()
    print(solution_part_one(problem_input))
    print(solution_part_two(problem_input))
