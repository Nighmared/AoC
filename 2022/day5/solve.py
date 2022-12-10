import os


def solve_puzzle(lines: "list[str]", move_boxes_one_at_a_time: bool) -> str:
    stacks_tmp: dict[int, list[str]] = {}
    input_line_indx = 0
    while (line := lines[input_line_indx].strip("\n")).strip().startswith("["):
        input_line_indx += 1
        col_indx = 0
        for a in range(1, len(line), 4):
            if line[a] == " ":
                col_indx += 1
                continue
            if col_indx in stacks_tmp:
                stacks_tmp[col_indx].append(line[a])
            else:
                stacks_tmp[col_indx] = [line[a]]
            col_indx += 1

    stacks: list[list[int]] = []
    for col_indx in range(0, len(stacks_tmp)):
        stacks_tmp[col_indx].reverse()
        stacks.append(stacks_tmp[col_indx])
    input_line_indx += 2
    for instruction_line in lines[input_line_indx:]:
        (
            _move,
            amount_s,
            _from,
            source_s,
            _to,
            target_s,
        ) = instruction_line.strip().split(" ")
        amount, source, target = map(int, [amount_s, source_s, target_s])
        source -= 1
        target -= 1
        tmp = stacks[source][-amount:]
        if move_boxes_one_at_a_time:
            tmp.reverse()
        stacks[source] = stacks[source][:-amount]
        stacks[target].extend(tmp)

    top_line = ""
    for stack in stacks:
        if len(stack) == 0:
            continue
        top_line += stack[-1]
    return top_line


def main():

    input_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(input_path, "r") as f:
        lines = f.readlines()

    part1 = solve_puzzle(lines, True)
    part2 = solve_puzzle(lines, False)
    print("Part 1: ", part1)
    print("Part 2: ", part2)


if __name__ == "__main__":
    main()
