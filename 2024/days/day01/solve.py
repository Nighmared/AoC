from collections import defaultdict

from inputreader.reader import InputReader
from solverbase import SolverBase


class Solver(SolverBase):

    class State:
        lines: list[str]
        left: list[int]
        cnt: dict[int, int]
        ran_p1: bool

    state: State

    def __init__(self, input_reader: InputReader) -> None:
        self.state = self.State()
        self.state.lines = input_reader.lines
        self.state.ran_p1 = False

    def part1(self) -> int:
        left = []
        right = []
        cnt: dict[int, int] = defaultdict(int)
        for line in self.state.lines:
            a, b = line.strip().split("  ")
            c, d = int(a), int(b)
            left.append(c)
            right.append(d)
            cnt[d] += 1

        assert len(left) == len(right)
        left_s = sorted(left)
        right_s = sorted(right)

        res = 0
        for i in range(len(left)):
            res += abs(left_s[i] - right_s[i])
        self.state.left = left
        self.state.cnt = cnt
        self.state.ran_p1 = True
        return res

    def part2(self) -> int:
        if not self.state.ran_p1:
            self.part1()
        res2 = 0
        for x in self.state.left:
            res2 += x * self.state.cnt[x]
        return res2


#####
