import os


def is_visible(matrix: list[list[int]], x: int, y: int) -> bool:
    if x == 0 or y == 0 or x == len(matrix[0]) - 1 or y == len(matrix) - 1:
        return True

    height = matrix[y][x]

    reachable = True
    i = x
    while i + 1 < len(matrix[0]):
        i += 1
        if matrix[y][i] >= height:
            reachable = False
            break
    if reachable:
        return True

    i = x
    reachable = True
    while i > 0:
        i -= 1
        if matrix[y][i] >= height:
            reachable = False
            break
    if reachable:
        return True

    j = y
    reachable = True
    while j + 1 < len(matrix):
        j += 1
        if matrix[j][x] >= height:
            reachable = False
            break
    if reachable:
        return True

    j = y
    reachable = True
    while j > 0:
        j -= 1
        if matrix[j][x] >= height:
            reachable = False
            break

    return reachable


def get_scenic_score(matrix: list[list[int]], x: int, y: int) -> int:
    if x == 0 or y == 0 or x == len(matrix[0]) - 1 or y == len(matrix) - 1:
        return 0
    height = matrix[y][x]

    scenic_right = 0
    while x + scenic_right + 1 < len(matrix[0]):
        scenic_right += 1
        if matrix[y][x + scenic_right] >= height:
            break

    scenic_left = 0
    while x - scenic_left > 0:
        scenic_left += 1
        if matrix[y][x - scenic_left] >= height:
            break

    scenic_down = 0
    while y + scenic_down + 1 < len(matrix):
        scenic_down += 1
        if matrix[y + scenic_down][x] >= height:
            break

    scenic_up = 0
    while y - scenic_up > 0:
        scenic_up += 1
        if matrix[y - scenic_up][x] >= height:
            break
    return scenic_up * scenic_down * scenic_left * scenic_right


def main():

    input_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(input_path, "r") as f:
        lines = f.readlines()
    matrix = []
    for line in lines:
        row = [int(t) for t in line.strip()]
        matrix.append(row)
    num_visible = 0
    best_scenic_score = 0
    for x in range(0, len(matrix[0])):
        for y in range(0, len(matrix)):
            scenic_score = get_scenic_score(matrix, x, y)
            if scenic_score > best_scenic_score:
                best_scenic_score = scenic_score
            if is_visible(matrix, x, y):
                num_visible += 1

    print("Part 1:", num_visible)
    print("Part 2:", best_scenic_score)


if __name__ == "__main__":
    main()
