from collections import defaultdict

from inputreader.reader import InputReader
from solverbase.SolverBase import SolverBase


class State:
    rules: list[tuple[int, int]]
    start_updates: int
    update_lines: list[str]
    bad_updates: list[list[int]]


class Page:
    page: int
    state: State

    def __init__(self, val: int, state: State) -> None:
        self.page = val
        self.state = state

    def __lt__(self, o) -> bool:
        if not isinstance(o, Page):
            raise TypeError("incomparable")

        if (self.page, o.page) in self.state.rules:
            return True
        return False

    def __repr__(self) -> str:
        return str(self.page)


class Solver(SolverBase):
    state: State

    def __init__(self, input_reader: InputReader) -> None:
        self.state = State()
        self.state.rules = []
        rule_d = defaultdict(set)
        self.state.rules = []
        self.state.bad_updates = []
        for i, l in enumerate(input_reader.lines):
            if l in ("\n", ""):
                start_updates = i + 1
                break
            a, b = l.split("|")
            rule_d[a].add(b)
            self.state.rules.append((int(a), int(b)))
        self.state.update_lines = input_reader.lines[start_updates:]

    def part1(self) -> int:
        good_updates: list[list[int]] = []
        for update in self.state.update_lines:
            if update.strip() == "":
                continue
            parsed = [int(x) for x in update.split(",")]
            for a, b in self.state.rules:
                if a in parsed and b in parsed:
                    if parsed.index(a) > parsed.index(b):
                        self.state.bad_updates.append(parsed)
                        break
            else:
                good_updates.append(parsed)

        sol1 = 0
        for gu in good_updates:
            sol1 += gu[len(gu) // 2]
        return sol1

    def part2(self) -> int:

        fixed_updates: list[list[Page]] = []
        for bu in self.state.bad_updates:
            pl = [Page(x, self.state) for x in bu]
            pl.sort()
            fixed_updates.append(pl)

        sol2 = 0
        for fu in fixed_updates:
            sol2 += fu[len(fu) // 2].page
        return sol2
