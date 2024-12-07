from operator import add, mul
from typing import Callable

from inputreader.reader import InputReader
from solverbase import SolverBase

operators1: list[Callable[[int, int], int]] = [mul, add]
operators2: list[Callable[[int, int], int]] = operators1 + [
    lambda x, y: int(str(x) + str(y))
]


def check_eq(
    first: int, rest: list[int], operators: list[Callable[[int, int], int]]
) -> bool:
    work_queue: set[tuple[int, int]] = {(rest[0], 1)}

    num_len = len(rest)
    while len(work_queue) > 0:
        next_l, next_d = work_queue.pop()
        if next_d == num_len:
            if first == next_l:
                return True
        else:
            for op in operators:
                next_res = op(next_l, rest[next_d])
                if next_res > first:
                    continue
                work_queue.add((next_res, next_d + 1))
    return False


class Solver(SolverBase):
    class State:
        equations: list[tuple[int, list[int]]]

    state: State

    def __init__(self, input_reader: InputReader) -> None:
        self.prints("Solving usually takes about 4 seconds")
        self.state = self.State()
        self.state.equations = []
        for line in input_reader.lines:
            first, rest = line.split(":")
            rest_i = [int(x) for x in rest.strip().split(" ")]
            self.state.equations.append((int(first), rest_i))

    def part1(self) -> int:
        res = 0
        for first, rest in self.state.equations:
            if check_eq(first, rest, operators1):
                res += first
        return res

    def part2(self) -> int:
        res = 0
        for first, rest in self.state.equations:
            if check_eq(first, rest, operators2):
                res += first
        return res
