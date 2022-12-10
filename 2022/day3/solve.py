import os


def main():

    input_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(input_path, "r") as f:
        lines = f.readlines()

    # Part One

    sum_dupe_priorities = 0
    for line in lines:
        mid_indx = len(line) // 2
        fst_comp = line[:mid_indx]
        snd_comp = line[mid_indx:]
        for item in fst_comp:
            if item in snd_comp:
                sum_dupe_priorities += get_priority(item)
                break
    print("Part 1: ", sum_dupe_priorities)

    # Part Two
    badge_priority_sum = 0
    for indx in range(0, len(lines), 3):
        elve_a, elve_b, elve_c = lines[indx : indx + 3]
        for item_a in elve_a:
            if item_a in elve_b and item_a in elve_c:
                badge_priority_sum += get_priority(item_a)
                break

    print("Part 2: ", badge_priority_sum)


def get_priority(letter: str) -> int:
    if ord(letter) > 96:
        # lower case, priorities from 1-26
        return ord(letter) - 96
    else:
        # upper case, priorities from 27-52
        return ord(letter) - 38


if __name__ == "__main__":
    main()
