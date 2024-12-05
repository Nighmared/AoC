with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

start_updates = -1
rules: list[tuple[int, int]] = []
for i, l in enumerate(lines):
    if l == "\n":
        start_updates = i + 1
        break
    a, b = l.split("|")
    rules.append((int(a), int(b)))

good_updates: list[list[int]] = []
bad_updates: list[list[int]] = []
for update in lines[start_updates:]:
    parsed = [int(x) for x in update.split(",")]
    for a, b in rules:
        if a in parsed and b in parsed:
            if parsed.index(a) > parsed.index(b):
                bad_updates.append(parsed)
                break
    else:
        good_updates.append(parsed)


sol1 = 0
for gu in good_updates:
    sol1 += gu[len(gu) // 2]

print("[Part 1]", sol1)


class Page:
    page: int

    def __init__(self, val: int) -> None:
        self.page = val

    def __lt__(self, o) -> bool:
        if not isinstance(o, Page):
            raise TypeError("incomparable")

        if (self.page, o.page) in rules:
            return True
        return False

    def __repr__(self) -> str:
        return str(self.page)


fixed_updates: list[list[Page]] = []
for bu in bad_updates:
    pl = [Page(x) for x in bu]
    pl.sort()
    fixed_updates.append(pl)


sol2 = 0
for fu in fixed_updates:
    sol2 += fu[len(fu) // 2].page

print("[Part 2]", sol2)
