for i in range(1, 7):
    with open(f"days/day{str(i).zfill(2)}/__init__.py", "w") as f:
        f.write("class Solver:\n    pass\n")
for i in range(7, 26):
    with open(f"days/day{str(i).zfill(2)}/__init__.py", "w") as f:
        f.write(f"from days.day{str(i).zfill(2)}.solve import Solver\n")
