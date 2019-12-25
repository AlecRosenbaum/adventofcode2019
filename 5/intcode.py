import enum
import attr


class ParamType(enum.Enum):
    POSITIONAL = enum.auto()
    IMMEDIATE = enum.auto()

    @classmethod
    def from_val(cls, val):
        if val:
            return cls.IMMEDIATE
        return cls.POSITIONAL


class Stop(Exception):
    pass


@attr.s
class Param(object):
    type_ = attr.ib()
    val = attr.ib()

    def get_val(self, program):
        if self.type_ == ParamType.IMMEDIATE:
            return self.val
        return program[self.val]


@attr.s
class Instruction(object):
    a = attr.ib(converter=ParamType.from_val)
    b = attr.ib(converter=ParamType.from_val)
    c = attr.ib(converter=ParamType.from_val)
    opcode = attr.ib()

    @classmethod
    def from_int(cls, val):
        a = (val // 10000) % 10
        b = (val // 1000) % 10
        c = (val // 100) % 10
        opcode = val % 100
        return cls(a=a, b=b, c=c, opcode=opcode)


@attr.s
class Command(object):
    CODE = None
    N_PARAMS = None

    instruction = attr.ib()
    params = attr.ib(factory=list)

    @classmethod
    def matches(cls, instruction):
        return instruction.opcode == cls.CODE

    def apply(self, state):
        self.run(state)
        state.instruction_pointer += self.N_PARAMS + 1

    def run(self, state):
        raise NotImplementedError()

    @classmethod
    def from_instruction(cls, instruction, state):
        ip = state.instruction_pointer

        return cls(
            instruction=instruction,
            params=[
                Param(
                    type_=getattr(instruction, {2: "a", 1: "b", 0: "c"}[i]),
                    val=state.program[ip + 1 + i],
                )
                for i in range(cls.N_PARAMS)
            ],
        )
        return cls(instruction=instruction)


@attr.s
class SumCmd(Command):
    CODE = 1
    N_PARAMS = 3

    def run(self, state):
        a, b, c = self.params
        assert c.type_ == ParamType.POSITIONAL

        state.program[c.val] = a.get_val(state.program) + b.get_val(state.program)
        return state


@attr.s
class MultCmd(Command):
    CODE = 2
    N_PARAMS = 3

    def run(self, state):
        a, b, c = self.params
        assert c.type_ == ParamType.POSITIONAL

        state.program[c.val] = a.get_val(state.program) * b.get_val(state.program)
        return state


@attr.s
class InputCmd(Command):
    CODE = 3
    N_PARAMS = 1

    def run(self, state):
        param = self.params[0]
        assert param.type_ == ParamType.POSITIONAL
        assert state.input_
        state.program[param.val] = state.input_.pop(0)
        return state


@attr.s
class OutputCmd(Command):
    CODE = 4
    N_PARAMS = 1

    def run(self, state):
        param = self.params[0]
        state.output.append(param.get_val(state.program))
        return state


@attr.s
class JumpIfTrueCmd(Command):
    CODE = 5
    N_PARAMS = 2

    def run(self, state):
        param, new_ip = self.params
        if param.get_val(state.program):
            state.instruction_pointer = new_ip.get_val(state.program) - (
                self.N_PARAMS + 1
            )
        return state


@attr.s
class JumpIfFalseCmd(Command):
    CODE = 6
    N_PARAMS = 2

    def run(self, state):
        param, new_ip = self.params
        if not param.get_val(state.program):
            state.instruction_pointer = new_ip.get_val(state.program) - (
                self.N_PARAMS + 1
            )
        return state


@attr.s
class LessThanCmd(Command):
    CODE = 7
    N_PARAMS = 3

    def run(self, state):
        a, b, result = self.params
        assert result.type_ == ParamType.POSITIONAL
        state.program[result.val] = (
            1 if a.get_val(state.program) < b.get_val(state.program) else 0
        )
        return state


@attr.s
class EqualsCmd(Command):
    CODE = 8
    N_PARAMS = 3

    def run(self, state):
        a, b, result = self.params
        assert result.type_ == ParamType.POSITIONAL
        state.program[result.val] = (
            1 if a.get_val(state.program) == b.get_val(state.program) else 0
        )
        return state


@attr.s
class HaltCmd(Command):
    CODE = 99
    N_PARAMS = 0

    def run(self, state):
        raise Stop()


@attr.s
class ProgramState(object):
    COMMANDS = [
        SumCmd,
        MultCmd,
        HaltCmd,
        InputCmd,
        OutputCmd,
        JumpIfTrueCmd,
        JumpIfFalseCmd,
        LessThanCmd,
        EqualsCmd,
    ]

    program = attr.ib(factory=list)
    instruction_pointer = attr.ib(default=0)
    input_ = attr.ib(factory=list)
    output = attr.ib(factory=list)

    @classmethod
    def from_csv(cls, data, noun=None, verb=None):
        program = list(map(int, data.split(",")))
        if noun is not None:
            program[1] = noun
        if verb is not None:
            program[2] = verb
        return cls(program=program)

    def step(self):
        for command in self.COMMANDS:
            instruction = Instruction.from_int(self.program[self.instruction_pointer])
            if command.matches(instruction):
                # self.print()
                command.from_instruction(instruction, self).apply(self)
                return
        raise ValueError(
            "Command matching {} not found".format(
                self.program[self.instruction_pointer]
            )
        )

    def print(self):
        print("=" * 15 * 6)
        for x in range(len(self.program) // 15):
            for y in range(15):
                idx = x * 15 + y
                if idx == self.instruction_pointer:
                    print(f"[{self.program[idx]:4}], ", end="")
                else:
                    print(f"{self.program[idx]:6}, ", end="")
            print("\n", end="")


def intcode(program, noun=None, verb=None, input_=None):
    state = ProgramState.from_csv(program, noun=noun, verb=verb)
    if input_:
        state.input_ = input_
    while True:
        try:
            state.step()
        except Stop:
            break
    return state
