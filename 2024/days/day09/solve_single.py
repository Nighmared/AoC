class Solver:

    blocks: list[tuple[int, int, int]]
    disk: list[int]

    def __init__(self, content) -> None:
        self.blocks = []
        free_block: bool = False
        self.disk = []
        block_id = 0
        for x in content:
            if free_block:
                self.disk += [-1] * int(x)
            else:
                block_len = int(x)
                self.blocks.append((len(self.disk), block_id, block_len))
                self.disk += [block_id] * block_len
                block_id += 1
            free_block = not free_block

    def part1(self) -> int:
        disk: list[int] = self.disk[::]
        disklen: int = len(disk)
        first_free: int = 0
        for j, block in enumerate(disk[::-1]):
            i = disklen - j - 1

            if block < 0:
                continue
            while disk[first_free] > -1:
                first_free += 1
                if first_free >= disklen:
                    break
            else:
                if i <= first_free:
                    break
                # print(f"moving {block} from {i} to {first_free}")
                disk[first_free] = block
                disk[i] = -1
                continue
            break
        res: int = 0
        for i, b in enumerate(disk):
            if b < 0:
                break
            res += i * b
        return res

    def part2(self) -> int:
        disk: list[int] = self.disk[::]
        free_list: list[list[int]] = []
        free_start: int = 0
        free_len: int = 0
        for i, b in enumerate(disk):
            if b < 0:
                if free_len == 0:
                    free_start = i
                free_len += 1
            else:
                if free_len > 0:
                    free_list.append([free_start, free_len])
                    free_len = 0

        for block_indx, block_id, block_len in self.blocks[::-1]:
            for freelistidx, (free_idx, free_len) in enumerate(free_list):
                if block_indx <= free_idx:
                    break
                if free_len >= block_len:
                    for i in range(block_len):
                        disk[block_indx + i] = -1
                        disk[free_idx + i] = block_id
                    if free_len > block_len:
                        free_list[freelistidx] = [
                            free_idx + block_len,
                            free_len - block_len,
                        ]
                    else:
                        free_list.pop(freelistidx)
                    break
            # for x in disk:
            #     if x < 0:
            #         print(".", end="")
            #     else:
            #         print(x, end="")
            # print()

        res = 0
        for i, b in enumerate(disk):
            if b < 0:
                continue
            res += i * b
        return res


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        cont = f.read().strip()
    cl = Solver(cont)
    #print(cl.part1())
    print(cl.part2())
