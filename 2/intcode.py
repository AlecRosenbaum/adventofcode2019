import attr


class Stop(Exception):
    pass


@attr.s
class Command(object):
    CODE = None
    N_PARAMS = None

    params = attr.ib(factory=list)

    def run(self, program):
        raise NotImplementedError()

    @classmethod
    def from_program(cls, program, ip):
        if cls.N_PARAMS:
            return cls(params=program[ip + 1 : ip + 1 + cls.N_PARAMS])
        return cls()


@attr.s
class SumCmd(Command):
    CODE = 1
    N_PARAMS = 3

    def run(self, program):
        a, b, c = self.params
        program[c] = program[a] + program[b]
        return program


@attr.s
class MultCmd(Command):
    CODE = 2
    N_PARAMS = 3

    def run(self, program):
        a, b, c = self.params
        program[c] = program[a] * program[b]
        return program


@attr.s
class HaltCmd(Command):
    CODE = 99
    N_PARAMS = 0

    def run(self, program):
        raise Stop()


COMMANDS = [SumCmd, MultCmd, HaltCmd]
CMD_LOOKUP = {cmd.CODE: cmd for cmd in COMMANDS}


def intcode(program, noun=None, verb=None):
    if noun is not None:
        program[1] = noun
    if verb is not None:
        program[2] = verb

    instruction_pointer = 0
    while True:
        command = CMD_LOOKUP[program[instruction_pointer]].from_program(
            program, instruction_pointer
        )
        try:
            program = command.run(program)
        except Stop:
            break
        instruction_pointer += command.N_PARAMS + 1

    return program
