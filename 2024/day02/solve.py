with open("input.txt", "r") as f:
    lines = f.readlines()

reports = [[int(x) for x in y.strip().split(" ")] for y in lines]


sol1 = 0
sol2 = 0


def pair_is_safe(a: int, b: int, ascending: bool) -> bool:
    if ascending:
        return 1 <= b - a <= 3
    else:
        return 1 <= a - b <= 3


def report_is_safe(r: list[int]) -> bool:
    ascending = True
    if r[0] == r[1]:
        return False
    ascending = r[0] < r[1]

    for i in range(0, len(r) - 1):
        if not pair_is_safe(r[i], r[i + 1], ascending):
            return False
    return True


for r in reports:

    if report_is_safe(r):
        sol1 += 1
        sol2 += 1
    else:
        for i in range(0, len(r)):
            cpy = r[::]
            cpy.pop(i)
            if report_is_safe(cpy):
                sol2 += 1
                break

print("[Part 1]", sol1)
print("[Part 2]", sol2)
