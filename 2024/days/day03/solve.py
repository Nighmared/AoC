"""Solution for Advent of Code 2024 Day 3"""

import re
from sys import exit as sysexit

from inputreader.reader import InputReader
from solverbase import SolverBase

PATTERN = r"(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))"


class State:
    res2: int
    mem_cont: str


class Solver(SolverBase):
    state: State

    def __init__(self, input_reader: InputReader) -> None:
        self.state = State()
        self.state.res2 = -1
        self.state.mem_cont = input_reader.content

    def part1(self) -> int:

        matches = re.findall(PATTERN, self.state.mem_cont)
        res1: int = 0
        res2: int = 0
        enabled: bool = True
        for instr in matches:
            if instr[0] != "":
                a, b = [int(x) for x in instr[0][4:-1].split(",")]
                res1 += (prod := a * b)
                if enabled:
                    res2 += prod
            elif instr[1] != "":
                enabled = True
            elif instr[2] != "":
                enabled = False
            else:
                print("AAAA")
                sysexit(-1)
        self.state.res2 = res2
        return res1

    def part2(self) -> int:
        if self.state.res2 < 0:
            self.part1()
        return self.state.res2
