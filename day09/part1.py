import argparse
import os
from copy import deepcopy
from collections import defaultdict

import pytest as pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_S = '''\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''


def adjacent(x, y):
    for x_d in (-1, 0, 1):
        for y_d in (-1, 0, 1):
            yield x + x_d, y + y_d


def compute(input_s: str) -> int:
    lines = input_s.strip().split('\n')
    x, y = 0, 0
    x_tail, y_tail = 0, 0
    tail_coords = defaultdict(int)
    tail_coords[x_tail, y_tail] += 1
    for line in lines:
        direction, length = line.split()
        length = int(length)
        if direction == 'R':
            for i in range(length):
                x_prev = x
                y_prev = y
                x += 1
                for other in adjacent(x_tail, y_tail):
                    if other == (x, y):
                        break
                else:
                    x_tail = x_prev
                    y_tail = y_prev
                    tail_coords[x_tail, y_tail] += 1
        elif direction == 'L':
            for i in range(length):
                x_prev = x
                y_prev = y
                x -= 1
                for other in adjacent(x_tail, y_tail):
                    if other == (x, y):
                        break
                else:
                    x_tail = x_prev
                    y_tail = y_prev
                    tail_coords[x_tail, y_tail] += 1
        elif direction == 'U':
            for i in range(length):
                x_prev = x
                y_prev = y
                y += 1
                for other in adjacent(x_tail, y_tail):
                    if other == (x, y):
                        break
                else:
                    x_tail = x_prev
                    y_tail = y_prev
                    tail_coords[x_tail, y_tail] += 1
        elif direction == 'D':
            for i in range(length):
                x_prev = x
                y_prev = y
                y -= 1
                for other in adjacent(x_tail, y_tail):
                    if other == (x, y):
                        break
                else:
                    x_tail = x_prev
                    y_tail = y_prev
                    tail_coords[x_tail, y_tail] += 1
    print(tail_coords)
    return len(tail_coords)


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
