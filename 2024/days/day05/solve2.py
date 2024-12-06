from collections import defaultdict

with open("input.txt", "r", encoding="utf-8") as f:
    cont = f.read()
rules, updates = [x.strip().split("\n") for x in cont.split("\n\n")]

rule_d = defaultdict(set)

for r in rules:
    update_parts, g = [int(x) for x in r.split("|")]
    rule_d[update_parts].add(g)


bad_updates: list[list[int]] = []
good_updates: list[list[int]] = []
sol1 = 0
for u in updates:
    update_parts = [int(x) for x in u.split(",")]
    for i, v in enumerate(update_parts[:-1]):
        for k in update_parts[i + 1 :]:
            if v in rule_d[k]:
                bad_updates.append(update_parts)
                break
        else:
            continue
        break
    else:
        sol1 += update_parts[len(update_parts) // 2]

print(sol1)
