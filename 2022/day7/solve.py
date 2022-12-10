import os


class FsElem:
    name: str
    parent: "Dir"
    type: str

    def get_size(self) -> int:
        raise NotImplemented("Dont call abstract base class")


class Dir(FsElem):
    children: list[FsElem]
    type = "dir"

    def __init__(self, name: str, parent: "Dir"):
        self.name = name
        self.children = []
        self.parent = parent

    def get_size(self):
        total = 0
        for child in self.children:
            total += child.get_size()
        return total

    def add_child(self, child: FsElem):
        self.children.append(child)

    def get_subdirs_max_size(self, max_size: int):
        res = []
        for child_dir in filter(lambda c: isinstance(c, Dir), self.children):
            res.extend(child_dir.get_subdirs_max_size(max_size))
            if child_dir.get_size() <= max_size:
                res.append(child_dir)
        return res

    def get_all_subdirs(self) -> list["Dir"]:
        res = []
        child_dirs: list[Dir] = list(
            filter(lambda c: isinstance(c, Dir), self.children)
        )
        res.extend(child_dirs)
        for child_dir in child_dirs:
            res.extend(child_dir.get_all_subdirs())
        return res


class Doc(FsElem):
    size: int
    type = "doc"

    def __init__(self, name: str, size: int, parent: Dir):
        self.name = name
        self.size = size
        self.parent = parent

    def get_size(self):
        return self.size


def build_tree(lines: list[str]) -> Dir:
    root: Dir = None
    current_dir: Dir = None
    for line in lines:
        if line.startswith("$"):
            # command
            parts = line.lstrip("$ ").strip().split(" ")
            command = parts[0]
            args = parts[1:]

            if command == "cd":
                # change directory
                target = args[0]
                if target == "/":
                    root = Dir("/", None)
                    current_dir = root
                elif target == "..":
                    if current_dir == None:
                        raise ValueError("nnonononono")
                    if current_dir == root:
                        # cant go higher
                        pass
                    else:
                        current_dir = current_dir.parent
                else:
                    target_dir = None
                    for child in filter(
                        lambda x: isinstance(x, Dir), current_dir.children
                    ):
                        if child.name == target:
                            target_dir = child
                            break
                    if target_dir is None:
                        raise ValueError("oof")
                    current_dir = target_dir
            elif command == "ls":
                # list
                pass
        else:
            if line.startswith("dir"):
                dirname = line.lstrip("dir").strip()
                # print("adding dir", dirname, "to dir", current_dir.name)
                current_dir.add_child(Dir(dirname, current_dir))
            else:
                size, filename = line.split(" ")
                # print(f"adding file {filename.strip()} to dir {current_dir.name}")
                current_dir.add_child(Doc(filename.strip(), int(size), current_dir))
    return root


def main():

    input_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(input_path, "r") as f:
        lines = f.readlines()

    root = build_tree(lines)

    # part 1
    limit = 100000
    candidate_dirs = []
    if root.get_size() <= limit:
        candidate_dirs.append(root)
    candidate_dirs.extend(root.get_subdirs_max_size(limit))
    sum_size = sum(map(lambda d: d.get_size(), candidate_dirs))
    print("Part 1:", sum_size)

    # part2
    total_space = 70000000
    needed_free = 30000000
    current_occupied_space = root.get_size()
    current_free_space = total_space - current_occupied_space
    dirs = root.get_all_subdirs()

    smallest_dir = root
    for dir in dirs:
        if current_free_space + dir.get_size() >= needed_free:
            if dir.get_size() < smallest_dir.get_size():
                smallest_dir = dir

    print("Part 2:", smallest_dir.get_size())


if __name__ == "__main__":
    main()
