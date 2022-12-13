with open("input.txt", "r") as f:
    lines = f.readlines()

elves = [0]
for line in lines:
    if line == "\n":
        elves.append(0)
    else:
        elves[-1] += int(line)


elves.sort()


print("================== PART 1 =================")

print("Elve carrying the most calories is carrying this many calories:")
print(elves[-1])


print("================== PART 2 =================")
print(
    "Amount of calories carried by the 3 elves that carry \nthe most, second most and third most:"
)
print(elves[-1] + elves[-2] + elves[-3])
