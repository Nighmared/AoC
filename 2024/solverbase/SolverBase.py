from abc import abstractmethod

from inputreader.reader import InputReader


class SolverBase:

    def __init__(self, input_reader: InputReader) -> None:
        raise NotImplementedError("Instantiating abstract base class")

    @abstractmethod
    def part1(self) -> int:
        """Returns solution for first Part of the daily puzzle"""

    @abstractmethod
    def part2(self) -> int:
        """Returns solution for second Part of the daily puzzle"""

    def prints(self, *arg, **kwargs):
        print("[Solver]", end=" ")
        print(*arg, **kwargs)
