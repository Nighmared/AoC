from typing import TypeVar, Union, Type
from typing import Callable


class Grid[T]:
    grid: list[list[T]]
    par_func: Callable[[str], T]
    atype: Type[T]
    w: int
    h: int

    def __init__(
        self,
        h: int,
        w: int,
        parsing_func: Callable[[str], T],
        empty_var: T,
        atype: Type[T],
    ):
        self.grid = [[empty_var] * w for _ in range(h)]
        self.par_func = parsing_func
        self.h = h
        self.w = w
        self.atype = atype

    def __getitem__(self, indx: tuple[int, int]) -> T:
        y, x = indx
        return self.grid[y][x]

    def __setitem__(self, key: tuple[int, int], val: Union[str, T]):
        if isinstance(val, str):
            val = self.par_func(val)
        y, x = key
        assert isinstance(val, self.atype)
        self.grid[y][x] = val

    def __str__(self) -> str:
        res = ""
        for y in range(self.h):
            res += " ".join([str(c) for c in self.grid[y]])
            if y < self.h - 1:
                res += "\n"
        return res

    def test(self, a: T) -> T:
        return a


if __name__ == "__main__":
    a: Grid[int] = Grid(10, 10, lambda x: int(x) * 2, 0)
    a.test("3")
