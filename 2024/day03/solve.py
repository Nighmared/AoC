"""Solution for Advent of Code 2024 Day 3"""

import re
from sys import exit as sysexit

with open("input.txt", "r", encoding="utf-8") as f:
    MEM_CONT = f.read()

PATTERN = r"(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))"

matches = re.findall(PATTERN, MEM_CONT)
res1: int = 0
res2: int = 0
enabled: bool = True
for instr in matches:
    if instr[0] != "":
        a, b = [int(x) for x in instr[0][4:-1].split(",")]
        res1 += (prod := a * b)
        if enabled:
            res2 += prod
    elif instr[1] != "":
        enabled: bool = True
    elif instr[2] != "":
        enabled: bool = False
    else:
        print("AAAA")
        sysexit(-1)
print("[Part 1]", res1)
print("[Part 2]", res2)
