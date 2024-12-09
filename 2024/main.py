from datetime import datetime
from sys import argv
from sys import exit as sysexit

import requests

import days
from inputreader import InputReader


def mk_input_path(day_nr: int, sample: bool = False) -> str:
    name = "sample.txt" if sample else "input.txt"
    return f"days/day{str(day_nr).zfill(2)}/{name}"


def download_and_store(day_nr: int) -> bool:
    with open("session.secret", "r", encoding="utf-8") as secret:
        session = secret.read().strip()

    resp = requests.get(
        f"https://adventofcode.com/2024/day/{day_nr}/input",
        cookies={"session": session},
        timeout=3,
    )
    if resp.status_code != 200:
        return False
    path = mk_input_path(day_nr=day_nr)
    with open(path, "w", encoding="utf-8") as file:
        file.write(resp.content.decode())
    return True


def main() -> None:
    # TODO good command parsing
    # with p1/p2 etc etc
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
    try:
        path = mk_input_path(day, sample)
        in_reader = InputReader(path)
    except FileNotFoundError:
        if sample:
            print("[!] Sample file not found, please store it at", path)
            sysexit(1)
        else:
            print("[?] Input file not found, trying to download")
            res = download_and_store(day)
            if not res:
                print("[!] Downloading failed. Are you too early? Exiting!")
                sysexit(1)
            else:
                print(f"[+] Downloaded input for day {day} and stored at {path}")
                in_reader = InputReader(path)

    solver = solver_cls(in_reader)
    res1 = solver.part1()
    if sample:
        print("[SAMPLE INPUT]", end="")
    print("[Part 1]", res1)
    res2 = solver.part2()
    if sample:
        print("[SAMPLE INPUT]", end="")
    print("[Part 2]", res2)


if __name__ == "__main__":
    main()
