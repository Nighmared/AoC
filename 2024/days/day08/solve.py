from collections import defaultdict

from inputreader.reader import InputReader
from solverbase import SolverBase


class Solver(SolverBase):

    class State:
        antennas: dict[str, list[tuple[int, int]]]
        antenna_coords: set[tuple[int, int]]
        max_x: int
        max_y: int
        sol2: int = -1

    state: State

    def __init__(self, input_reader: InputReader) -> None:
        self.state = self.State()
        self.state.antennas = defaultdict(list)
        self.state.antenna_coords = set()
        for i, line in enumerate(input_reader.lines):
            for j, c in enumerate(line):
                if c != ".":
                    self.state.antenna_coords.add((i, j))
                    self.state.antennas[c].append((i, j))

        self.state.max_y = len(input_reader.lines)
        self.state.max_x = len(input_reader.lines[0])

    def part1(self) -> int:
        antinodes: set[tuple[int, int]] = set()
        antinodes2: set[tuple[int, int]] = set(self.state.antenna_coords)
        for v in self.state.antennas.values():
            for i, (yi, xi) in enumerate(v[:-1]):
                for yj, xj in v[i + 1 :]:
                    ydiff = yi - yj
                    xdiff = xi - xj
                    keep_going = True
                    it = 1
                    while keep_going:
                        keep_going = False
                        antinode_candidates = (
                            (yi + it * ydiff, xi + it * xdiff),
                            (yj - it * ydiff, xj - it * xdiff),
                        )
                        for yc, xc in antinode_candidates:
                            if (
                                0 <= yc < self.state.max_y
                                and 0 <= xc < self.state.max_x
                            ):
                                keep_going = True
                                antinodes2.add((yc, xc))
                                if it == 1:
                                    antinodes.add((yc, xc))
                        it += 1
        self.state.sol2 = len(antinodes2)
        return len(antinodes)

    def part2(self) -> int:
        if self.state.sol2 < 0:
            self.part1()
        return self.state.sol2
