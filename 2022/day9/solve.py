import os
from collections import defaultdict
from typing import Optional

import pydantic


class Knot(pydantic.BaseModel):
    visited: dict[int, set] = defaultdict(set)
    prev_x: int = 0
    prev_y: int = 0
    x: int = 0
    y: int = 0
    follow: Optional["Knot"]
    next: "Knot" = None
    name: str  # only for debugging

    def visit_current_pos(self):
        self.visited[self.x].add(self.y)

    def move(self, direction: str):
        self.prev_x, self.prev_y = (
            self.x,
            self.y,
        )
        if direction == "R":
            self.x += 1
        elif direction == "L":
            self.x -= 1
        elif direction == "U":
            self.y += 1
        elif direction == "D":
            self.y -= 1
        self.visited[self.x].add(self.y)

    def _move_to(self, x: int, y: int):
        self.prev_x, self.prev_y = self.x, self.y
        self.x = x
        self.y = y
        self.visited[self.x].add(self.y)

    def follow_knot(self, other_knot: "Knot"):
        if (other_knot.x - self.x) ** 2 <= 1 and (other_knot.y - self.y) ** 2 <= 1:
            # dont do anything if other_knot is still in one of the 9 adjacent coords (or on same)
            # aka dont do anything if sum of squared dists in x and y is <=2
            return
        # diagonal
        if self.x != other_knot.x and self.y != other_knot.y:
            if (self.x - other_knot.x) ** 2 > 1:
                if self.y > other_knot.y:
                    new_y = self.y - 1
                else:
                    new_y = self.y + 1

                if self.x > other_knot.x:
                    self._move_to(self.x - 1, new_y)
                elif self.x < other_knot.x:
                    self._move_to(self.x + 1, new_y)
            else:
                if self.x > other_knot.x:
                    new_x = self.x - 1
                else:
                    new_x = self.x + 1

                new_y = (self.y - 1) if (self.y > other_knot.y) else (self.y + 1)
                self._move_to(new_x, new_y)
            return
        # below the case where only one coord differs
        if self.x != other_knot.x:
            if self.x < other_knot.x:
                self._move_to(self.x + 1, self.y)
            else:
                self._move_to(self.x - 1, self.y)
            return
        if self.y != other_knot.y:
            if self.y < other_knot.y:
                self._move_to(self.x, self.y + 1)
            else:
                self._move_to(self.x, self.y - 1)
            return

        raise ValueError("how on earth did we get here")

    def do_follow(self):
        self.follow_knot(self.follow)
        if self.next is not None:
            self.next.do_follow()

    def number_visited(self) -> int:
        sum_visitied = 0
        for _key, y_set in self.visited.items():
            sum_visitied += len(y_set)
        return sum_visitied


def main():

    input_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(input_path, "r") as f:
        lines = f.readlines()

    head = Knot(follow=None, name="head")
    tail = Knot(follow=head, name="tail")

    tail.visit_current_pos()

    for line in lines:
        direction, steps = line.split(" ")
        # call move and do_follow 'steps' many times
        for _i in range(0, int(steps)):
            head.move(direction)
            tail.do_follow()

    print("Part 1:", tail.number_visited())

    # PART 2 ===================================
    head = Knot(follow=None, name="head")
    last_node = head
    for i in range(0, 9):
        new_knot = Knot(follow=last_node, name=str(i + 1))
        last_node.next = new_knot
        last_node = new_knot
        new_knot.visit_current_pos()

    for line in lines:
        direction, steps = line.split(" ")
        for i in range(0, int(steps)):
            head.move(direction)
            # this propagates the call through all the following knots
            head.next.do_follow()

    # dynamically get to tail
    current: Knot = head
    while current.next is not None:
        current = current.next

    print("Part 2:", current.number_visited())


if __name__ == "__main__":
    main()
