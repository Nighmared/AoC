from inputreader.reader import InputReader
from solverbase.SolverBase import SolverBase


class Solver(SolverBase):
    class State:
        lines: list[str]

    state: State

    def __init__(self, input_reader: InputReader) -> None:
        self.state = self.State()
        self.state.lines = input_reader.lines

    def part1(self) -> int:
        return -1

    def part2(self) -> int:
        return -1
