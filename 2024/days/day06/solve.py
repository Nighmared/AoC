from inputreader.reader import InputReader
from solverbase.SolverBase import SolverBase

DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))


class State:
    grid: list[list[str]]
    start_x: int
    start_y: int
    max_y: int
    max_x: int
    visited_cells: set[tuple[int, int]]
    obstacles: set[tuple[int, int]]


class Solver(SolverBase):
    state: State

    def __init__(self, input_reader: InputReader) -> None:
        self.state = State()
        self.state.grid = [list(line.strip()) for line in input_reader.lines]
        self.state.max_y = len(self.state.grid)
        self.state.max_x = len(self.state.grid[0])
        print("Part 2 takes a while")

    def part1(self) -> int:
        coord_y = -1
        coord_x = -1
        curr_direction_idx: int = 0

        self.state.obstacles = set()
        for i, line in enumerate(self.state.grid):
            if "^" in line:
                coord_y = i
                coord_x = line.index("^")
            for j, c in enumerate(line):
                if c == "#":
                    self.state.obstacles.add((i, j))

        assert coord_x != -1 and coord_y != -1
        self.state.start_x = coord_x
        self.state.start_y = coord_y

        visited_cells: set[tuple[int, int]] = set()

        visited_cells.add((coord_y, coord_x))
        while 0 <= coord_y < self.state.max_y and 0 <= coord_x < self.state.max_x:
            next_y = coord_y + DIRECTIONS[curr_direction_idx][0]
            next_x = coord_x + DIRECTIONS[curr_direction_idx][1]
            try:
                if (next_y, next_x) in self.state.obstacles:
                    curr_direction_idx = (curr_direction_idx + 1) % 4
                else:
                    coord_y = next_y
                    coord_x = next_x
                    visited_cells.add((coord_y, coord_x))
            except IndexError:
                break
        self.state.visited_cells = visited_cells
        return len(visited_cells)

    def part2(self) -> int:
        cycle_coords = 0
        visited_dir: set[tuple[int, int, int]] = set()
        i = 0
        for obst_y, obst_x in self.state.visited_cells:
            if (self.state.start_x, self.state.start_y) == (obst_x, obst_y):
                continue
            i += 1
            # print(str(i).zfill(4), f"/{len(self.state.visited_cells)}", end="\r")
            coord_y = self.state.start_y
            coord_x = self.state.start_x
            curr_direction_idx = 0
            visited_dir.clear()
            next_y = coord_y + DIRECTIONS[curr_direction_idx][0]
            next_x = coord_x + DIRECTIONS[curr_direction_idx][1]
            while 0 <= next_y < self.state.max_y and 0 <= next_x < self.state.max_x:
                visited_dir.add((coord_y, coord_x, curr_direction_idx))
                if (next_y, next_x) in self.state.obstacles or (
                    next_y == obst_y and next_x == obst_x
                ):
                    curr_direction_idx = (curr_direction_idx + 1) % 4
                else:
                    coord_y = next_y
                    coord_x = next_x
                    if (coord_y, coord_x, curr_direction_idx) in visited_dir:
                        cycle_coords += 1
                        break
                next_y = coord_y + DIRECTIONS[curr_direction_idx][0]
                next_x = coord_x + DIRECTIONS[curr_direction_idx][1]
        return cycle_coords
