from inputreader.reader import InputReader
from solverbase import SolverBase


class Solver(SolverBase):
    class State:
        disk: list[int]
        blocks: list[tuple[int, int, int]]

    state: State

    def __init__(self, input_reader: InputReader) -> None:
        self.state = self.State()
        self.state.blocks = []
        free_block = False
        disk: list[int] = []
        block_id = 0
        for x in input_reader.content:
            if free_block:
                disk += [-1] * int(x)
            else:
                block_len = int(x)
                self.state.blocks.append((len(disk), block_id, block_len))
                disk += [block_id] * block_len
                block_id += 1
            free_block = not free_block
        self.state.disk = disk

    def part1(self) -> int:
        disk = self.state.disk[::]
        disklen = len(disk)
        first_free = 0
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
        res = 0
        for i, b in enumerate(disk):
            if b < 0:
                break
            res += i * b
        return res

    def part2(self) -> int:
        disk = self.state.disk[::]
        disklen = len(disk)
        for block_indx, block_id, block_len in self.state.blocks[::-1]:
            if block_id % 500 == 0:
                print(block_id)
            free_len = 0
            free_indx = 0
            progress = True
            while free_len < block_len and free_indx < disklen and progress:
                progress = False
                if free_indx + free_len >= disklen:
                    break
                if disk[free_indx] > -1:
                    free_indx += 1
                    free_len = 0
                    progress = True
                elif disk[free_indx + free_len] < 0:
                    free_len += 1
                    progress = True
                if not progress:
                    free_indx += 1
                    free_len = 0
                    progress = True
            if free_indx == disklen:
                continue
            if block_indx <= free_indx:
                continue
            if block_len <= free_len:
                for i in range(block_len):
                    disk[free_indx + i] = block_id
                    disk[block_indx + i] = -1
                free_len -= block_len

        res = 0
        for i, b in enumerate(disk):
            if b < 0:
                continue
            res += i * b
        return res
