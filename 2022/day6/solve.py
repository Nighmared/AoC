import os


def detect_marker(stream: str, marker_len: int) -> int:
    """Returns index of first character in stream after a sequence
    of 'marker_len' different characters"""
    indx = marker_len
    window_chars = stream[:indx]
    keep_loop = True
    while indx + 1 < len(stream) and keep_loop:
        # check wether all 4 different
        seen = []
        for char in window_chars:
            if char not in seen:
                seen.append(char)
        if len(seen) == marker_len:
            keep_loop = False
        indx += 1
        # only update window if there will be a next iteration
        if keep_loop:
            window_chars = window_chars[1:] + stream[indx]
    return indx


def main():

    input_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(input_path, "r") as f:
        stream = f.read()

    part1 = detect_marker(stream, 4)
    part2 = detect_marker(stream, 14)

    print("Part 1: ", part1)
    print("Part 2: ", part2)


if __name__ == "__main__":
    main()
