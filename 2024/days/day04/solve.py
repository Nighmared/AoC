"""Solution for Advent of Code 2024 Day 4"""

from enum import Enum, auto

from inputreader.reader import InputReader
from solverbase.SolverBase import SolverBase


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    DIAGRU = auto()
    DIAGRD = auto()
    DIAGLD = auto()
    DIAGLU = auto()


def check_at_coords(grid: list[list[str]], x: int, y: int, dir: Direction) -> bool:
    GOAL = "XMAS"
    if dir in (Direction.LEFT, Direction.DIAGLD, Direction.DIAGLU):
        if x < 3:
            return False

    if dir in (Direction.DIAGRD, Direction.DIAGRU, Direction.RIGHT):
        if x > len(grid[0]) - 4:
            return False

    if dir in (Direction.DOWN, Direction.DIAGLD, Direction.DIAGRD):
        if y > len(grid) - 4:
            return False
    if dir in (Direction.UP, Direction.DIAGLU, Direction.DIAGRU):
        if y < 3:
            return False
    steps = (0, 0)
    if dir == Direction.LEFT:
        steps = (0, -1)
    elif dir == Direction.RIGHT:
        steps = (0, 1)
    elif dir == Direction.DOWN:
        steps = (1, 0)
    elif dir == Direction.UP:
        steps = (-1, 0)
    elif dir == Direction.DIAGLD:
        steps = (1, -1)
    elif dir == Direction.DIAGRD:
        steps = (1, 1)
    elif dir == Direction.DIAGLU:
        steps = (-1, -1)
    elif dir == Direction.DIAGRU:
        steps = (-1, 1)
    else:
        print("AAAAA")
        exit(42)

    start_x, start_y = (x, y)
    step_y, step_x = steps
    for i in GOAL:
        if grid[start_y][start_x] != i:
            return False
        start_x += step_x
        start_y += step_y
    return True


class State:
    grid: list[list[str]]


class Solver(SolverBase):
    def __init__(self, input_reader: InputReader) -> None:
        self.state = State()
        self.state.grid = [list(line.strip()) for line in input_reader.lines]
        if self.state.grid[-1] == []:
            self.state.grid.pop(-1)

    def part1(self) -> int:
        num_xmas = 0
        for y, row in enumerate(self.state.grid):
            for x in range(len(row)):
                if self.state.grid[y][x] == "X":
                    for d in Direction:
                        if check_at_coords(self.state.grid, x, y, d):
                            num_xmas += 1
        return num_xmas

    def part2(self) -> int:
        num_cross: int = 0
        ms_set: set[str] = {"M", "S"}
        y_lim = len(self.state.grid) - 1
        x_lim = len(self.state.grid[0]) - 1
        for y, row in enumerate(self.state.grid):
            for x, c in enumerate(row):
                if y == y_lim or x == x_lim or y == 0 or x == 0:
                    continue
                if c == "A":
                    if (
                        {self.state.grid[y - 1][x - 1], self.state.grid[y + 1][x + 1]}
                        == ms_set
                    ) and (
                        {self.state.grid[y - 1][x + 1], self.state.grid[y + 1][x - 1]}
                        == ms_set
                    ):
                        num_cross += 1

        return num_cross
