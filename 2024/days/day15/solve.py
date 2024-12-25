from inputreader.reader import InputReader
from solverbase import SolverBase
from enum import Enum, auto
from lib import Grid


class Instruction(Enum):
    DOWN = "v"
    UP = "^"
    LEFT = "<"
    RIGHT = ">"


class FieldType(Enum):
    WALL = "#"
    EMPTY = "."
    BOX = "O"
    ROBOT = "@"

    def __str__(self) -> str:
        return self.value


class Solver(SolverBase):

    grid: Grid[FieldType]

    def __init__(self, input_reader: InputReader) -> None:
        h = 0
        for l in input_reader.lines:
            if l.strip() == "":
                break
            h += 1
        w = len(input_reader.lines[0])

        self.grid = Grid(h, w, FieldType, FieldType.EMPTY, FieldType)
        for y, l in enumerate(input_reader.lines[:h]):
            for x, c in enumerate(l):
                self.grid[y, x] = c

        print(self.grid)
        instrs = "".join(input_reader.lines[h + 1 :])
        print(instrs)

        pass

    def part1(self) -> int:
        print(FieldType("#"))
        return -1

    def part2(self) -> int:
        return -1
