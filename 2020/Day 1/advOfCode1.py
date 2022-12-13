lines = open("advOfCode1.txt").readlines()
vals = []
for line in lines:
    vals.append(int(line))


# Part 1
for i in range(0, len(vals)):
    for j in range(i, len(vals)):
        if vals[i] + vals[j] == 2020:
            print("Result for part 1: ", vals[i] * vals[j])
            break

# Part 2
solved = False
for i in range(0, len(vals)):
    if solved:
        break
    for j in range(i, len(vals)):
        if solved:
            break
        tmpSum = vals[i] + vals[j]
        if tmpSum >= 2020:
            continue
        for k in range(j, len(vals)):
            if tmpSum + vals[k] == 2020:
                print("Result for part 2: ", vals[i] * vals[j] * vals[k])
                solved = True
                break
