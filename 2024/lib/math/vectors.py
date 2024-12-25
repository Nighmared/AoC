from dataclasses import dataclass
from math import sqrt


def numeric_second_arg(f):
    def new_func(slf, arg):
        if not isinstance(arg, (int, float)):
            raise TypeError(
                f"Can only call {f.__qualname__} with numeric type as second argument. Found {type(arg).__name__}"
            )
        return f(slf, arg)

    return new_func


@dataclass
class Vector2:
    x: int
    y: int
    iter_idx: int = -1

    @staticmethod
    def all_args_vector2_type(f):
        def new_func(*args):
            for a in args:
                if not isinstance(a, Vector2):
                    raise TypeError(
                        f"all arguments to {f.__qualname__} must be of type Vector2 but found {type(a).__name__}"
                    )

    @all_args_vector2_type
    def __sub__(self, o):
        return Vector2(self.x - o.x, self.y - o.y)

    @all_args_vector2_type
    def __add__(self, o):
        return Vector2(self.x + o.x, self.y + o.y)

    @all_args_vector2_type
    def __iadd__(self, o):
        self.x += o.x
        self.y += o.y

        return self

    @all_args_vector2_type
    def __isub__(self, o):
        self.x -= o.x
        self.y -= o.y
        return self

    @numeric_second_arg
    def __mul__(self, o):
        return Vector2(self.x * o, self.y * o)

    @numeric_second_arg
    def __imul__(self, o):
        self.x *= o
        self.y *= o
        return self

    @numeric_second_arg
    def __div__(self, o):
        return Vector2(self.x / o, self.y / o)

    @numeric_second_arg
    def __idiv__(self, o):
        self.x /= o
        self.y /= o
        return self

    @numeric_second_arg
    def __mod__(self, o):
        return Vector2(self.x % o, self, y % o)

    @numeric_second_arg
    def __imod__(self, o):
        self.x %= o
        self.y %= o
        return self

    def abs_sum(self):
        return abs(self.x) + abs(self.y)

    def length(self) -> float:
        return sqrt(self.x**2 + self.y**2)

    def __len__(self) -> float:
        return self.length()

    def to_tuple(self):
        return (self.y, self.x)

    def __iter__(self):
        return iter([self.x, self.y])


class Vec3:
    pass
