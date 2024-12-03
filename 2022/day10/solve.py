import os
from itertools import cycle
from time import sleep


class Processor:
    x: int = 1
    cycle: int = 1
    crt_pos: int = 0

    interesting_x = {
        20: None,
        60: None,
        100: None,
        140: None,
        180: None,
        220: None,
    }

    def crt_cycle(self):
        EMTPY_CHAR = " "  # is "." in the original task
        FULL_CHAR = "█"  # is "#" in the original
        if abs(self.x - self.crt_pos) < 2:
            print(FULL_CHAR, end="", flush=True)
        else:
            print(EMTPY_CHAR, end="", flush=True)
        self.crt_pos += 1
        if self.crt_pos == 40:
            self.crt_pos = 0
            print()
        sleep(0.004)

    def execute(self, line: str):

        self.crt_cycle()
        self._check_interesting()

        parts = line.strip().split(" ")
        cmd = parts[0]
        arg = None
        if len(parts) > 1:
            arg = int(parts[1])
        if cmd == "noop":
            self.cycle += 1
            return
        elif cmd == "addx":
            self.cycle += 1
            self._check_interesting()
            self.cycle += 1
            self.crt_cycle()
            self._check_interesting()
            self.x += arg

    def _check_interesting(self):
        if self.cycle in self.interesting_x:
            self.interesting_x[self.cycle] = self.x

    def get_sum_strengths(self):
        res = 0
        for (cycle, x_val) in self.interesting_x.items():
            res += cycle * x_val
        return res


def main():

    input_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(input_path, "r") as f:
        lines = f.readlines()

    proc = Processor()
    print(
        "\n==========================================================================="
    )
    print("PART 2: (read letters)")
    print()
    for line in lines:
        proc.execute(line)
    print()
    print()
    print(
        "=========================================================================== \n"
    )
    print("Part 1:")
    print(">>", proc.get_sum_strengths(), "<<")


if __name__ == "__main__":
    main()
