from sys import argv


class Solver:
    results_grid: list[list[set[tuple[int, int]]]]
    rating_grid: list[list[int]]
    grid: list[list[int]]
    starts: list[tuple[int, int]]
    limy: int
    limx: int
    sol2: int

    def __init__(self, inputl: list[str]) -> None:
        self.starts = []
        self.grid = []
        self.results_grid = []
        self.rating_grid = []
        self.sol2 = -1
        for y, line in enumerate(inputl):
            self.grid.append([])
            self.results_grid.append([])
            self.rating_grid.append([])
            for x, c in enumerate(line):
                ci = int(c)
                if ci == 0:
                    self.starts.append((y, x))
                if ci == 9:
                    self.results_grid[-1].append({(y, x)})
                    self.rating_grid[-1].append(1)
                else:
                    self.results_grid[-1].append(set())
                    self.rating_grid[-1].append(-1)
                self.grid[-1].append(ci)

        self.limy = len(self.grid)
        self.limx = len(self.grid[0])

    def rec_part1(self, curr_pos_y, curr_pos_x) -> tuple[set[tuple[int, int]], int]:
        cached: set[tuple[int, int]] = self.results_grid[curr_pos_y][curr_pos_x]
        cached2: int = self.rating_grid[curr_pos_y][curr_pos_x]
        if len(cached) > 0:
            return cached, cached2

        curr_val: int = self.grid[curr_pos_y][curr_pos_x]

        dirs = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]
        sol = set()
        sol2 = 0
        for dy, dx in dirs:
            if (
                0 <= (ny := curr_pos_y + dy) < self.limy
                and 0 <= (nx := curr_pos_x + dx) < self.limx
            ):
                if self.grid[ny][nx] == curr_val + 1:
                    res1, res2 = self.rec_part1(ny, nx)
                    sol |= res1
                    sol2 += res2
        self.results_grid[curr_pos_y][curr_pos_x] = sol
        self.rating_grid[curr_pos_y][curr_pos_x] = sol2
        return sol, sol2

    def part1(self) -> int:
        sol = 0
        sol2 = 0
        for zy, zx in self.starts:
            rs = self.rec_part1(zy, zx)
            sol += len(rs[0])  # number of distinct peaks reachable
            sol2 += rs[1]  # number of distinct paths to reach a peak
        self.sol2 = sol2
        return sol

    def part2(self) -> int:
        if self.sol2 < 0:
            self.part1()
        return self.sol2


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        ls = file.read().strip().split("\n")
    sl = Solver(ls)

    if "1" in argv[1]:
        print(sl.part1())
    if "2" in argv[1]:
        print(sl.part2())
