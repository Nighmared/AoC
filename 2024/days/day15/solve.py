from inputreader.reader import InputReader
from solverbase import SolverBase


class State:
    pass


class Solver(SolverBase):
    state: State
    input_reader: InputReader

    def __init__(self, input_reader: InputReader) -> None:
        self.state = State()
        self.input_reader = input_reader

    def part1(self) -> int:
        return -1

    def part2(self) -> int:
        return -1
