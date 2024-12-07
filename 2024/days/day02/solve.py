from inputreader.reader import InputReader
from solverbase import SolverBase


def pair_is_safe(a: int, b: int, ascending: bool) -> bool:
    if ascending:
        return 1 <= b - a <= 3
    else:
        return 1 <= a - b <= 3


def report_is_safe(r: list[int]) -> bool:
    ascending = True
    if r[0] == r[1]:
        return False
    ascending = r[0] < r[1]

    for i in range(0, len(r) - 1):
        if not pair_is_safe(r[i], r[i + 1], ascending):
            return False
    return True


class State:
    res2: int
    reports: list[list[int]]


class Solver(SolverBase):
    state: State

    def __init__(self, input_reader: InputReader) -> None:
        self.state = State()
        self.state.res2 = -1
        self.state.reports = [
            [int(x) for x in y.strip().split(" ")] for y in input_reader.lines
        ]

    def part1(self) -> int:
        sol1 = 0
        sol2 = 0
        for r in self.state.reports:
            if report_is_safe(r):
                sol1 += 1
                sol2 += 1
            else:
                for i in range(0, len(r)):
                    cpy = r[::]
                    cpy.pop(i)
                    if report_is_safe(cpy):
                        sol2 += 1
                        break

        self.state.res2 = sol2
        return sol1

    def part2(self) -> int:
        if self.state.res2 < 0:
            self.part1()
        return self.state.res2
