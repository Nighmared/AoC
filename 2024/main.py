from sys import argv

import days
from inputreader import InputReader


def mk_input_path(day_nr: int, sample: bool = False) -> str:
    name = "sample.txt" if sample else "input.txt"
    return f"days/day{str(day_nr).zfill(2)}/{name}"


def main():
    assert len(argv) > 1
    sample: bool = False
    if len(argv) == 3:
        sample: bool = True
        print("[*] Using sample input because a third argument is present")
    day = int(argv[1])
    solver_cls = days.days[day]
    solver = solver_cls(InputReader(mk_input_path(day, sample)))
    print("[Part 1]", solver.part1())
    print("[Part 2]", solver.part2())


if __name__ == "__main__":
    main()
