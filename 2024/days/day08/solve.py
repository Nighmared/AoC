from collections import defaultdict

from inputreader.reader import InputReader
from solverbase import SolverBase


class Solver(SolverBase):

    class State:
        antennas: dict[str, list[tuple[int, int]]]
        antenna_coords: set[tuple[int, int]]
        max_x: int
        max_y: int

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
        for v in self.state.antennas.values():
            vlen = len(v)
            for i in range(vlen - 1):
                for j in range(i + 1, vlen):
                    yi, xi = v[i]
                    yj, xj = v[j]
                    ydiff = yi - yj
                    xdiff = xi - xj
                    antinode_candidates = (
                        (yi + ydiff, xi + xdiff),
                        (yj - ydiff, xj - xdiff),
                    )
                    for yc, xc in antinode_candidates:
                        if 0 <= yc < self.state.max_y and 0 <= xc < self.state.max_x:
                            antinodes.add((yc, xc))
        return len(antinodes)

    def part2(self) -> int:
        antinodes: set[tuple[int, int]] = set(self.state.antenna_coords)
        for v in self.state.antennas.values():
            vlen = len(v)
            for i in range(vlen - 1):
                # self.prints(k, "antenna at", v[i])
                for j in range(i + 1, vlen):
                    # self.prints("->", k, "antenna at", v[j])
                    yi, xi = v[i]
                    yj, xj = v[j]
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
                                # self.prints(f"creates antinode at ({yc},{xc})")
                                keep_going = True
                                antinodes.add((yc, xc))
                        it += 1
        return len(antinodes)
