from datetime import datetime
from sys import argv

import days
from inputreader import InputReader


def mk_input_path(day_nr: int, sample: bool = False) -> str:
    name = "sample.txt" if sample else "input.txt"
    return f"days/day{str(day_nr).zfill(2)}/{name}"


def main() -> None:
    day = -1
    if (
        (len(argv) == 1 or (len(argv) == 2 and not argv[-1].isnumeric()))
        and (now := datetime.today()).year == 2024
        and now.month == 12
        and now.day < 26
    ):
        day = now.day
        print(f"[*] Defaulting to day {day} (Today) because no day was specified")
    else:
        day = int(argv[1])
    sample: bool = False
    if argv[-1] in ("s", "sample", "debug", "test", "-s"):
        sample = True
        print("[*] Using sample input because last argument is a flag for it")
    solver_cls = days.days[day]
    solver = solver_cls(InputReader(mk_input_path(day, sample)))
    if sample:
        print("[SAMPLE INPUT]", end="")
    print("[Part 1]", solver.part1())
    if sample:
        print("[SAMPLE INPUT]", end="")
    print("[Part 2]", solver.part2())


if __name__ == "__main__":
    main()
