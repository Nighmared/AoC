"""Solution for Advent of Code 2024 Day 4"""

from enum import Enum, auto


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    DIAGRU = auto()
    DIAGRD = auto()
    DIAGLD = auto()
    DIAGLU = auto()


class Xmas:
    start: tuple[int, int]
    direction: Direction

    def __init__(self, start: tuple[int, int], direction: Direction) -> None:
        self.start = start
        self.direction = direction

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Xmas):
            return False
        return self.start == value.start and self.direction == value.direction


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

    start_x, start_y = (x, y)
    step_y, step_x = steps
    for i in GOAL:
        if grid[start_y][start_x] != i:
            return False
        start_x += step_x
        start_y += step_y
    return True


with open("input.txt", "r", encoding="utf-8") as f:
    LINES = f.readlines()
    RAW_CONT = f.read()
print(f"[?] Input has {len(LINES)} lines")
# Solution goes here

grid = []
for line in LINES:
    grid.append(list(line))

SOL1: int = 0
SOL2: int = 0

num_xmas = 0
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if grid[y][x] == "X":
            for d in Direction:
                if check_at_coords(grid, x, y, d):
                    num_xmas += 1
SOL1 = num_xmas


#####

num_cross: int = 0
ms_set: set[str] = {"M", "S"}
for y, row in enumerate(LINES):
    for x, c in enumerate(row):
        if y == len(grid) - 1 or x == len(row) - 1 or y == 0 or x == 0:
            continue
        if c == "A":
            if ({LINES[y - 1][x - 1], LINES[y + 1][x + 1]} == ms_set) and (
                {LINES[y - 1][x + 1], LINES[y + 1][x - 1]} == ms_set
            ):
                num_cross += 1

SOL2 = num_cross

####################

print("[Part 1]", SOL1)
print("[Part 2]", SOL2)
