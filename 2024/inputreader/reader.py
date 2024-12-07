class InputReader:
    fname: str
    lines: list[str]
    content: str

    def __init__(self, fpath) -> None:
        self.fname = fpath
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                self.content = f.read()
                self.lines = self.content.split("\n")
                if self.lines[-1].strip() == "":
                    self.lines.pop()
        except FileNotFoundError:
            print("No such file", fpath)
