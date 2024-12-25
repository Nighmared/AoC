from collections import defaultdict
from inputreader.reader import InputReader
from solverbase import SolverBase
from dataclasses import dataclass
from time import sleep


@dataclass
class Vec2:
    x: int
    y: int

    def __mul__(self, o):
        if not isinstance(o, int):
            raise TypeError
        return Vec2(self.x * o, self.y * o)

    def __add__(self, o):
        if not isinstance(o, Vec2):
            raise TypeError
        return Vec2(self.x + o.x, self.y + o.y)

    @staticmethod
    def from_tuple_xy(x: tuple[int, int]):
        return Vec2(x[0], x[1])


@dataclass
class Robot:
    start: Vec2
    v: Vec2


def sim(r: Robot, t: int) -> Vec2:
    return r.start + r.v * t


def sim_mod(r: Robot, t: int, w: int, h: int) -> Vec2:
    res = sim(r, t)
    return Vec2(res.x % w, res.y % h)


class Solver(SolverBase):
    robots: list[Robot]

    def __init__(self, input_reader: InputReader) -> None:
        self.robots = []
        for l in input_reader.lines:
            p, v = [[int(y) for y in x[2:].split(",")] for x in l.split(" ")]
            self.robots.append(Robot(Vec2.from_tuple_xy(p), Vec2.from_tuple_xy(v)))

    def part1(self) -> int:
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        w = 101
        h = 103
        half_w = w // 2
        half_h = h // 2
        for r in self.robots:
            after_sim = sim_mod(r, 100, w, h)
            if after_sim.x < half_w:
                if after_sim.y < half_h:
                    q1 += 1
                elif after_sim.y > half_h:
                    q3 += 1
            elif after_sim.x > half_w:
                if after_sim.y < half_h:
                    q2 += 1
                elif after_sim.y > half_h:
                    q4 += 1
        return q1 * q2 * q3 * q4

    def part2(self) -> int:
        w = 101
        h = 103
        printcnt = 0
        min_dist = 10000
        for i in range(0, 10_000):
            sumx = 0
            map = [[0] * w for _ in range(h)]
            for r in self.robots:
                p = sim_mod(r, i, w, h)
                sumx += p.x
                map[p.y][p.x] += 1

            # for y in range(0, h):
            #     cnt = 0
            #     for x in range(30, 60):
            #         cnt += map[y][x]
            #     if cnt > 10:
            #         break
            # else:
            #     continue
            sum_hor_dist = 0
            for r in map:
                curr_dist = 0
                for c in r:
                    if c > 0:
                        sum_hor_dist += curr_dist
                        curr_dist = 0
                    else:
                        curr_dist += 1
            avgdist = sum_hor_dist / len(self.robots)
            min_dist = min(avgdist, min_dist)
            if avgdist < 11:
                printcnt += 1
                print("=" * 100)
                print(i)
                for j in range(h):
                    print(str(j).zfill(3), end=" ")
                    for k in range(w):
                        c = map[j][k]
                        if c > 0:
                            print("█", end="")
                        else:
                            print(" ", end="")
                    print()
                return i
        raise ValueError("Did not find tree!")
