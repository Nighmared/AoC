from Computer2 import Computer

solver = Computer("input.txt")

print("part1 solution: ")
solver.inval = 1
solver.work()

print("part2 solution: ")
solver.reset()
solver.inval = 5
solver.work()
