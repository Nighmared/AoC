from days.day01 import Solver as Solver1
from days.day02 import Solver as Solver2
from days.day03 import Solver as Solver3
from days.day04 import Solver as Solver4
from days.day05 import Solver as Solver5
from days.day06 import Solver as Solver6
from days.day07 import Solver as Solver7
from days.day08 import Solver as Solver8
from days.day09 import Solver as Solver9
from days.day10 import Solver as Solver10
from days.day11 import Solver as Solver11
from days.day12 import Solver as Solver12
from days.day13 import Solver as Solver13
from days.day14 import Solver as Solver14
from days.day15 import Solver as Solver15
from days.day16 import Solver as Solver16
from days.day17 import Solver as Solver17
from days.day18 import Solver as Solver18
from days.day19 import Solver as Solver19
from days.day20 import Solver as Solver20
from days.day21 import Solver as Solver21
from days.day22 import Solver as Solver22
from days.day23 import Solver as Solver23
from days.day24 import Solver as Solver24
from days.day25 import Solver as Solver25
from solverbase import SolverBase

days: dict[int, type[SolverBase]] = {
    1: Solver1,
    2: Solver2,
    3: Solver3,
    4: Solver4,
    5: Solver5,
    6: Solver6,
    7: Solver7,
    8: Solver8,
    9: Solver9,
    10: Solver10,
    11: Solver11,
    12: Solver12,
    13: Solver13,
    14: Solver14,
    15: Solver15,
    16: Solver16,
    17: Solver17,
    18: Solver18,
    19: Solver19,
    20: Solver20,
    21: Solver21,
    22: Solver22,
    23: Solver23,
    24: Solver24,
    25: Solver25,
}
