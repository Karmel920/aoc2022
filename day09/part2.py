import argparse
import os
from collections import defaultdict
from copy import deepcopy

import pytest as pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_S = '''\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
'''


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
        self.prev = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.score = defaultdict(int)
        self.score[0, 0] += 1

    def is_empty(self) -> bool:
        return self.head is None

    def printing(self):
        print_value = self.head
        while print_value is not None:
            print(print_value.x, print_value.y)
            print_value = print_value.next

    def get_node(self, index: int):
        if self.is_empty() or index < 0:
            raise IndexError(f'Index out of bounds: {index}')

        current_node = self.head
        current_index = index
        while current_index > 0:
            if current_node is None:
                raise IndexError(f'Index out of bounds: {index}')
            current_node = current_node.next
            current_index -= 1

        return current_node

    def add(self, index, x, y):
        if self.head is None and index == 0:
            self.head = Node(x, y)
            self.tail = self.head
            return True

        node_at_index = self.get_node(index)

        if node_at_index is None:
            previous_tail = self.tail
            self.tail = Node(x, y)
            self.tail.prev = previous_tail
            previous_tail.next = self.tail
            return True

        if node_at_index.prev is None:
            previous_head = self.head
            self.head = Node(x, y)
            self.head.next = previous_head
            previous_head.prev = self.head
            return True

        new_node = Node(x, y)
        previous = node_at_index.prev
        previous.next = new_node
        new_node.previous = previous

        new_node.next = node_at_index
        node_at_index.prev = new_node
        return True

    def move(self, direction):
        if direction == 'R':
            self.head.x += 1
        elif direction == 'L':
            self.head.x -= 1
        elif direction == 'U':
            self.head.y += 1
        elif direction == 'D':
            self.head.y -= 1

        current = self.head
        while current.next is not None:
            for other in adjacent(current.next):
                if other == current:
                    break
            else:
                changed = False
                for new_pos in column(current.next):
                    for other in column(new_pos):
                        if other == current:
                            new_pos.prev = current.next.prev
                            new_pos.next = current.next.next
                            current.next = new_pos
                            changed = True
                            # print("Wchodzimy column")
                            # self.printing()
                            # print("Wychodzimy column")
                            break
                    if changed:
                        break
                else:
                    for new_pos in row(current.next):
                        for other in row(new_pos):
                            if other == current:
                                new_pos.prev = current.next.prev
                                new_pos.next = current.next.next
                                current.next = new_pos
                                changed = True
                                # print("Wchodzimy row")
                                # self.printing()
                                # print("Wychodzimy row")
                                break
                        if changed:
                            break
                    else:
                        for new_pos in diagonal(current.next):
                            for other in adjacent(new_pos):
                                if other == current:
                                    new_pos.prev = current.next.prev
                                    new_pos.next = current.next.next
                                    current.next = new_pos
                                    changed = True
                                    # print("Wchodzimy diagonal")
                                    # self.printing()
                                    # print("Wychodzimy diagonal")
                                    break
                            if changed:
                                break
            current = current.next
        self.score[current.x, current.y] += 1


def adjacent(node):
    for x_d in (-1, 0, 1):
        for y_d in (-1, 0, 1):
            yield Node(node.x + x_d, node.y + y_d)


def diagonal(node):
    for x_d in (-1, 1):
        for y_d in (-1, 1):
            yield Node(node.x + x_d, node.y + y_d)


def column(node):
    for x_d in (-1, 1):
        yield Node(node.x + x_d, node.y)


def row(node):
    for y_d in (-1, 1):
        yield Node(node.x, node.y + y_d)


def compute(input_s: str) -> int:
    lines = input_s.strip().split('\n')
    knots = LinkedList()
    for i in range(10):
        knots.add(i, 0, 0)

    for line in lines:
        direction, length = line.split()
        length = int(length)
        for i in range(length):
            knots.move(direction)

    return len(knots.score)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        # print(compute(INPUT_S))
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    main()
