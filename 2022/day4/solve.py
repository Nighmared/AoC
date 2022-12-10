import os


def main():

    input_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(input_path, "r") as f:
        lines = f.readlines()

    num_pairs_contained = 0
    num_overlap_pairs = 0
    for line in lines:
        elve_a, elve_b = line.split(",")
        low_a, up_a = map(int, elve_a.split("-"))
        low_b, up_b = map(int, elve_b.split("-"))
        if (low_a <= low_b and up_a >= up_b) or (low_b <= low_a and up_b >= up_a):
            num_pairs_contained += 1

        if (low_a <= low_b and up_a >= low_b) or (low_b <= low_a and up_b >= low_a):
            num_overlap_pairs += 1

    print("Part 1: ", num_pairs_contained)
    print("Part 2: ", num_overlap_pairs)


if __name__ == "__main__":
    main()
