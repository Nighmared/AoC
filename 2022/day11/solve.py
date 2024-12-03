import os
from typing import Optional
import pydantic
from numpy import lcm


class Operator(pydantic.BaseModel):
    value: int

    def apply(self, i: int) -> int:
        raise NotImplemented("Abstract method called")


class MultOp(Operator):
    def apply(self, i: int) -> int:
        return self.value * i


class AddOp(Operator):
    def apply(self, i: int) -> int:
        return self.value + i


class SubOp(Operator):
    def apply(self, i: int) -> int:
        return self.value - i


class DivOp(Operator):
    def apply(self, i: int) -> int:
        return i // self.value


class SquareOp(Operator):
    def apply(self, i: int) -> int:
        return i * i


class Monkey(pydantic.BaseModel):
    number: int
    items: list[int]
    operation_line: str
    operation: Operator
    div_check: int
    next_true: int
    next_false: int
    monkey_map: dict
    items_inspected: int = 0
    calm_down: bool = True
    modd: Optional[bool]

    def __str__(self) -> str:
        return f"Monkey({self.number=}, {self.items=}, {self.operation=}, {self.div_check=}, {self.next_true=}, {self.next_false=})"

    def catch(self, item: int):
        self.items.append(item % self.modd)

    def one_item(self):
        item = self.items.pop(0)
        self.items_inspected += 1
        item_o = item
        item = self.operation.apply(item)
        if self.calm_down:
            item //= 3
        # if item%self.div_check == 0 returns the monkey with id == self.next_true, otherwise monkey with id == self.next_false
        next_monkey_id = (self.next_false, self.next_true)[item % self.div_check == 0]
        # print(f"monkey {self.number} throws {item} (was {item_o}) to {next_monkey_id}")
        next_monkey = self.monkey_map[next_monkey_id]
        next_monkey.catch(item)

    def get_inspected(self):
        print(f"{self.number} inspected {self.items_inspected}")

    def play_all_items(self):
        while len(self.items) > 0:
            self.one_item()


def read_input(lines, calm_down: bool = True) -> dict[int, Monkey]:

    prod_div_checks = 1
    indx = 0
    monkey_map: dict[int, Monkey] = dict()
    while indx < len(lines):
        line = lines[indx]
        if line.startswith("Monkey"):
            monkey_id = int(line.split(" ")[1].strip().rstrip(":"))
            indx += 1
            line = lines[indx]
            items = list(map(int, line.strip().lstrip("Starting items: ").split(",")))
            indx += 1
            line = lines[indx]
            operation_ine = line
            op_parts = (
                line.strip()
                .lstrip("Operation:")
                .strip()
                .lstrip("new")
                .strip()
                .lstrip("=")
                .strip()
                .lstrip("old")
                .strip()
                .split(" ")
            )
            op, value = op_parts
            if value.strip() == "old":
                operator = SquareOp(value=0)
            elif op == "+":
                operator = AddOp(value=int(value))
            elif op == "-":
                operator = SubOp(value=int(value))
            elif op == "*":
                operator = MultOp(value=int(value))
            elif op == "/":
                operator = DivOp(value=int(value))
            else:
                raise ValueError("wtf is this operation " + op)

            indx += 1
            line = lines[indx]
            div_check = int(line.strip().lstrip("Test: divisible by "))
            prod_div_checks = lcm(prod_div_checks, div_check)
            indx += 1
            line = lines[indx]
            next_true = int(line.split(" ")[-1])
            indx += 1

            line = lines[indx]
            next_false = int(line.split(" ")[-1])
            monkey_map[monkey_id] = Monkey(
                number=monkey_id,
                next_true=next_true,
                next_false=next_false,
                operation=operator,
                div_check=div_check,
                items=items,
                monkey_map=monkey_map,
                operation_line=operation_ine,
                calm_down=calm_down,
            )

        indx += 1
    for monke in monkey_map.values():
        monke.modd = prod_div_checks
    return monkey_map


def main():

    input_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(input_path, "r") as f:
        lines = f.readlines()

    monkey_map = read_input(
        lines,
    )

    num_rounds = 20
    for _i in range(0, num_rounds):
        print(
            f"Round {_i+1}/{num_rounds}",
            end="\r",
        )
        for monkey in monkey_map.values():
            monkey.play_all_items()
    print()
    ordered_monkey = [monkey_map[id] for id in sorted(monkey_map.keys())]

    busyness = [x.items_inspected for x in ordered_monkey]
    busyness.sort()
    print(busyness[-1] * busyness[-2])

    #############################################

    monkey_map = read_input(lines, calm_down=False)
    num_rounds = 10_000
    for _i in range(0, num_rounds):
        print(
            f"Round {_i+1}/{num_rounds}",
            end="\r",
        )
        for monkey in monkey_map.values():
            monkey.play_all_items()
    print()
    ordered_monkey = [monkey_map[id] for id in sorted(monkey_map.keys())]

    busyness = [x.items_inspected for x in ordered_monkey]
    busyness.sort()
    print(busyness[-1] * busyness[-2])


if __name__ == "__main__":
    main()
