from dataclasses import dataclass
from inputreader.reader import InputReader
from solverbase import SolverBase
from sympy import Matrix
from sympy.core.numbers import Integer


@dataclass
class Game:
    button1: tuple[int, int]
    button2: tuple[int, int]
    target: tuple[int, int]


class Solver(SolverBase):
    games: list[Game]

    def __init__(self, input_reader: InputReader) -> None:
        self.games = []
        for i in range(0, len(input_reader.lines), 4):
            b1x, b1y = input_reader.lines[i].split(":")[1].split(",")
            b1x = int(b1x.split("+")[1])
            b1y = int(b1y.split("+")[1])
            b2x, b2y = input_reader.lines[i + 1].split(":")[1].split(",")
            b2x = int(b2x.split("+")[1])
            b2y = int(b2y.split("+")[1])
            gx, gy = input_reader.lines[i + 2].split(":")[1].split(",")
            gx = int(gx.split("=")[1])
            gy = int(gy.split("=")[1])
            self.games.append(Game((b1x, b1y), (b2x, b2y), (gx, gy)))

    def part1(self) -> int:
        cost = 0
        for g in self.games:
            A = Matrix(
                [
                    [g.button1[0], g.button2[0], g.target[0]],
                    [g.button1[1], g.button2[1], g.target[1]],
                ]
            )
            n1, n2 = A.nullspace()[0][:2]
            if (not isinstance(n1, Integer)) or (not isinstance(n2, Integer)):
                continue
            cost += -3 * n1 + -1 * n2
            print(-n1, -n2, -3 * n1 + -1 * n2)
        return cost

    def part2(self) -> int:
        cost = 0
        for g in self.games:
            g.target = (g.target[0] + 10000000000000, g.target[1] + 10000000000000)

            A = Matrix(
                [
                    [g.button1[0], g.button2[0], g.target[0]],
                    [g.button1[1], g.button2[1], g.target[1]],
                ]
            )
            n1, n2 = A.nullspace()[0][:2]
            if (not isinstance(n1, Integer)) or (not isinstance(n2, Integer)):
                continue
            cost += -3 * n1 + -1 * n2
            print(-n1, -n2, -3 * n1 + -1 * n2)
        return cost
