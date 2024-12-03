import re

with open("input.txt", "r") as f:
    mem_cont = f.read()
# mem_cont = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

pattern = r"(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))"

valid_instrs = re.findall(pattern, mem_cont)


res1 = 0
res2 = 0
enabled = True
for instr in valid_instrs:
    if instr[0] != "":
        a, b = [int(x) for x in instr[0][4:-1].split(",")]
        res1 += (prod := a * b)
        if enabled:
            res2 += prod
    elif instr[1] != "":
        enabled = True
    elif instr[2] != "":
        enabled = False
    else:
        print("AAAA")
print("[Part 1]", res1)


print("[Part 2]", res2)
