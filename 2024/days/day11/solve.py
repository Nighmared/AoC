from collections import defaultdict
from math import ceil, log10

from inputreader.reader import InputReader
from solverbase import SolverBase


class Solver(SolverBase):
    stones_in: list[int]

    def __init__(self, input_reader: InputReader) -> None:
        self.stones_in = [int(x) for x in input_reader.content.split(" ")]

    def _sim_stones(self, iter_count: int) -> int:
        """Simulates the stone rules for `iter_count` iterations
        and then returns the number of stones"""
        old: dict[int, int] = dict([(x, 1) for x in self.stones_in])
        new: dict[int, int] = defaultdict(int)
        for _ in range(iter_count):
            new.clear()
            for stone, cnt in old.items():
                new_vals: list[int] = []
                if stone == 0:
                    new_vals = [1]
                else:
                    num_exp: int = int(log10(stone))
                    num_digits: int = num_exp + 1
                    if num_digits % 2 == 0:  # if number of digits is even
                        sep: int = 10 ** (ceil(num_exp / 2))
                        first = stone // sep
                        sec = stone % sep
                        new_vals = [first, sec]
                    else:
                        new_vals = [stone * 2024]
                for n in new_vals:
                    new[n] += cnt
            old = dict(new)
        assert len(old) == len(new)
        res = 0
        for v in old.values():
            res += v
        return res

    def part1(self) -> int:
        self.prints("P1 should be 189547")
        return self._sim_stones(25)

    def part2(self) -> int:
        return self._sim_stones(75)
