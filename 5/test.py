import pytest

from solution import solution_part_one, solution_part_two

from intcode import ProgramState, Stop, Instruction


# @pytest.mark.parametrize(
#     "x,expected",
#     [
#         ("1,9,10,3,2,3,11,0,99,30,40,50", "3500,9,10,70,2,3,11,0,99,30,40,50"),
#         ("1,0,0,0,99", "2,0,0,0,99"),
#         ("2,3,0,3,99", "2,3,0,6,99"),
#         ("2,4,4,5,99,0", "2,4,4,5,99,9801"),
#         ("1,1,1,4,99,5,6,0,99", "30,1,1,4,2,5,6,0,99"),
#     ],
# )
# def test_solution_part_one(x, expected):
#     assert expected == solution_part_one(x)


def test_input_and_output():
    state = ProgramState.from_csv("3,0,4,0,99")
    state.input_.append(90)
    while True:
        try:
            state.step()
        except Stop:
            break
    assert state.output == [90]


@pytest.mark.parametrize(
    "x,expected",
    [
        (1002, Instruction(a=0, b=1, c=0, opcode=2)),
        (1102, Instruction(a=0, b=1, c=1, opcode=2)),
        (2, Instruction(a=0, b=0, c=0, opcode=2)),
    ],
)
def test_instruction(x, expected):
    assert expected == Instruction.from_int(x)


def test_immediate_mode():
    state = ProgramState.from_csv("1002,4,3,4,33")
    while True:
        try:
            state.step()
        except Stop:
            break
    assert state.program == [1002, 4, 3, 4, 99]


@pytest.mark.parametrize(
    "program,input_,expected_output",
    [
        ("3,9,8,9,10,9,4,9,99,-1,8", [9], [0]),
        ("3,9,8,9,10,9,4,9,99,-1,8", [8], [1]),
        ("3,9,8,9,10,9,4,9,99,-1,8", [7], [0]),
        ("3,9,7,9,10,9,4,9,99,-1,8", [9], [0]),
        ("3,9,7,9,10,9,4,9,99,-1,8", [8], [0]),
        ("3,9,7,9,10,9,4,9,99,-1,8", [7], [1]),
        ("3,3,1108,-1,8,3,4,3,99", [9], [0]),
        ("3,3,1108,-1,8,3,4,3,99", [8], [1]),
        ("3,3,1108,-1,8,3,4,3,99", [7], [0]),
        ("3,3,1107,-1,8,3,4,3,99", [9], [0]),
        ("3,3,1107,-1,8,3,4,3,99", [8], [0]),
        ("3,3,1107,-1,8,3,4,3,99", [7], [1]),
        ("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", [0], [0]),
        ("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", [1], [1]),
        ("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", [10], [1]),
        ("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", [-10], [1]),
        ("3,3,1105,-1,9,1101,0,0,12,4,12,99,1", [0], [0]),
        ("3,3,1105,-1,9,1101,0,0,12,4,12,99,1", [1], [1]),
        ("3,3,1105,-1,9,1101,0,0,12,4,12,99,1", [10], [1]),
        ("3,3,1105,-1,9,1101,0,0,12,4,12,99,1", [-10], [1]),
        ("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99", [6], [999]),
        ("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99", [8], [1000]),
        ("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99", [10], [1001]),
    ],
)
def test_program(program, input_, expected_output):
    state = ProgramState.from_csv(program)
    state.input_ = input_
    while True:
        try:
            state.step()
        except Stop:
            break
    assert expected_output == state.output


# @pytest.mark.parametrize("x,expected", [("14", 2), ("1969", 966), ("100756", 50346)])
# def test_solution_part_one(x, expected):
#     assert expected == solution_part_two(x)
