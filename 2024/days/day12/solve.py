from dataclasses import dataclass
from functools import cache
from inputreader.reader import InputReader
from solverbase import SolverBase
from enum import Enum, auto
from collections import defaultdict


class SideFacing(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


def all_args_same_type(f):
    def new_func(*args):
        goal_type = type(args[0])
        for i, a in enumerate(args[1:]):
            if not isinstance(a, goal_type):
                raise TypeError(
                    f"Argument Number {i+1} to {f.__qualname__} must have type {goal_type.__name__} but is of type {type(a).__name__}"
                )
        return f(*args)

    return new_func


@dataclass
class Vector2:
    x: int
    y: int

    @all_args_same_type
    def __sub__(self, o):
        return Vector2(self.x - o.x, self.y - o.y)

    @all_args_same_type
    def __add__(self, o):
        return Vector2(self.x + o.x, self.y + o.y)

    def abs_sum(self):
        return abs(self.x) + abs(self.y)

    def to_tuple(self):
        return (self.y, self.x)


ONE_RIGHT = Vector2(1, 0)
ONE_LEFT = Vector2(-1, 0)
ONE_DOWN = Vector2(0, 1)
ONE_UP = Vector2(0, -1)


class Plot:
    cells: list[tuple[int, int]]
    grid: list[list[int]]
    charac: int
    plot_id: int

    def __init__(self, charac: int, grid: list[list[int]], plot_id: int):
        self.cells = []
        self.charac = charac
        self.grid = grid
        self.plot_id = plot_id

    @cache
    def __is_edge_piece(self, y: int, x: int) -> bool:
        if x == 0 or x == len(self.grid[0]) - 1:
            return True
        if y == 0 or y == len(self.grid) - 1:
            return True
        if (
            (self.grid[y - 1][x] != self.charac)
            or (self.grid[y + 1][x] != self.charac)
            or (self.grid[y][x + 1] != self.charac)
            or (self.grid[y][x - 1] != self.charac)
        ):
            return True
        return False

    def __get_facing(self, y, x) -> set[SideFacing]:
        assert self.__is_edge_piece(y, x)
        faces: set[SideFacing] = set()
        if y == 0 or self.grid[y - 1][x] != self.charac:
            faces.add(SideFacing.UP)
        if y == len(self.grid) - 1 or self.grid[y + 1][x] != self.charac:
            faces.add(SideFacing.DOWN)
        if x == 0 or self.grid[y][x - 1] != self.charac:
            faces.add(SideFacing.LEFT)
        if x == len(self.grid[0]) - 1 or self.grid[y][x + 1] != self.charac:
            faces.add(SideFacing.RIGHT)
        return faces

    @cache
    def area(self) -> int:
        return len(self.cells)

    @cache
    def sides(self) -> int:
        candidates: list[tuple[int, int]] = []
        for y, x in self.cells:
            if self.__is_edge_piece(y, x):
                candidates.append((y, x))
        edges: dict[SideFacing, list[tuple[int, int]]] = {
            SideFacing.UP: [],
            SideFacing.DOWN: [],
            SideFacing.LEFT: [],
            SideFacing.RIGHT: [],
        }
        for cand in candidates:
            fa = self.__get_facing(cand[0], cand[1])
            for f in fa:
                edges[f].append(cand)

        separate_edges: list[tuple[SideFacing, list[tuple[int, int]]]] = []

        matching = (
            (SideFacing.UP, ONE_LEFT, ONE_RIGHT),
            (SideFacing.DOWN, ONE_LEFT, ONE_RIGHT),
            (SideFacing.LEFT, ONE_UP, ONE_DOWN),
            (SideFacing.RIGHT, ONE_UP, ONE_DOWN),
        )
        e_cnt = 0
        seen_sum = 0
        for dir, backward_modifier, forward_modifier in matching:
            curr_iter_edges: list[tuple[SideFacing, list[tuple[int, int]]]] = []

            edge_map: dict[tuple[int, int], list[tuple[int, int]]] = {}
            edges[dir].sort()
            for c in edges[dir]:
                curr_v = Vector2(c[1], c[0])
                if (look_back := (curr_v + backward_modifier).to_tuple()) in edge_map:
                    edge_map[look_back].append(c)
                    edge_map[c] = edge_map[look_back]
                else:
                    edge_map[c] = [c]
            print(chr(self.charac), dir)
            seen = []
            for x in edge_map.values():
                if x not in seen:
                    e_cnt += 1
                    seen.append(x)
            print(len(seen), seen)
            seen_sum += len(seen)

        print(seen_sum)

        return e_cnt

    @cache
    def perimeter(self) -> int:
        per = 0
        for y, x in self.cells:
            if y > 0:
                if self.grid[y - 1][x] != self.charac:
                    per += 1
            else:
                per += 1
            if y < len(self.grid) - 1:
                if self.grid[y + 1][x] != self.charac:
                    per += 1
            else:
                per += 1
            if x > 0:
                if self.grid[y][x - 1] != self.charac:
                    per += 1
            else:
                per += 1
            if x < len(self.grid[0]) - 1:
                if self.grid[y][x + 1] != self.charac:
                    per += 1
            else:
                per += 1
        return per

    @all_args_same_type
    def __add__(self, o):
        if self.charac != o.charac:
            raise ValueError("Character mismatch")

        new_plot = Plot(self.charac, self.grid, self.plot_id)
        all_cells = set(self.cells + o.cells)
        for y, x in all_cells:
            new_plot.cells.append((y, x))
        return new_plot


class Solver(SolverBase):
    grid: list[list[int]]
    plot_grid: list[list[int]]
    plot_map: dict[int, Plot]

    def __init__(self, input_reader: InputReader) -> None:
        self.grid = []
        self.plot_grid = []
        self.plot_map = {}
        for line in input_reader.lines:
            curr = []
            for c in line:
                curr.append(ord(c))
            self.plot_grid.append([-1] * len(curr))
            self.grid.append(curr)

    def part1(self) -> int:
        plot_key = 0
        for y, l in enumerate(self.grid):
            for x, c in enumerate(l):
                same_crop: list[tuple[int, int]] = []
                if y > 0:
                    if self.grid[y - 1][x] == c:  # same crop
                        same_crop.append((y - 1, x))
                if x > 0:
                    if self.grid[y][x - 1] == c:
                        same_crop.append((y, x - 1))
                to_modify = None
                if len(same_crop) == 0:
                    new_plot = Plot(c, self.grid, plot_key)
                    self.plot_map[plot_key] = new_plot
                    plot_key += 1
                    to_modify = new_plot
                if len(same_crop) == 1:
                    to_modify = self.plot_map[
                        self.plot_grid[same_crop[0][0]][same_crop[0][1]]
                    ]
                if len(same_crop) == 2:
                    coords_a = same_crop[0]
                    coords_b = same_crop[1]
                    plot_a = self.plot_map[self.plot_grid[coords_a[0]][coords_a[1]]]
                    plot_b = self.plot_map[self.plot_grid[coords_b[0]][coords_b[1]]]

                    if plot_a == plot_b:
                        to_modify = plot_a
                    else:
                        to_modify = plot_a + plot_b
                        self.plot_map.pop(plot_a.plot_id)
                        self.plot_map.pop(plot_b.plot_id)
                        to_modify.plot_id = plot_key
                        plot_key += 1
                        self.plot_map[to_modify.plot_id] = to_modify
                        for c in to_modify.cells:
                            self.plot_grid[c[0]][c[1]] = to_modify.plot_id

                if to_modify is not None:
                    self.plot_grid[y][x] = to_modify.plot_id
                    to_modify.cells.append((y, x))
                else:
                    raise ValueError("Hä")

        r = 0
        for v in self.plot_map.values():
            r += v.area() * v.perimeter()

        return r

    def part2(self) -> int:

        r = 0
        for v in self.plot_map.values():
            print(chr(v.charac), v.area(), v.sides(), v.area() * v.sides())
            r += v.area() * v.sides()
        return r
