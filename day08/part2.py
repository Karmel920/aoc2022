import argparse
import os
from collections import defaultdict
from copy import deepcopy

import pytest as pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_S = '''\
30373
25512
65332
33549
35390
'''


def left(x, y):
    for x_d in range(x - 1, -1, -1):
        yield x_d, y


def right(x, y, m):
    for x_d in range(x + 1, m + 1, 1):
        yield x_d, y


def top(x, y):
    for y_d in range(y - 1, -1, -1):
        yield x, y_d


def bottom(x, y, n):
    for y_d in range(y + 1, n + 1, 1):
        yield x, y_d


def compute(input_s: str) -> int:
    coords = defaultdict(int)
    n, m = 0, 0
    for y, line in enumerate(input_s.strip().split('\n')):
        n = y
        for x, height in enumerate(line):
            coords[x, y] = int(height)
            m = x

    scenic_score = 0

    for x in range(m + 1):
        for y in range(n + 1):
            if x == 0:
                continue
            elif y == 0:
                continue
            elif x == m:
                continue
            elif y == n:
                continue
            else:
                score_top = 0
                score_bottom = 0
                score_right = 0
                score_left = 0
                for other in top(x, y):
                    if coords[other] < coords[x, y]:
                        score_top += 1
                    if coords[other] >= coords[x, y]:
                        score_top += 1
                        break
                for other in bottom(x, y, m):
                    if coords[other] < coords[x, y]:
                        score_bottom += 1
                    if coords[other] >= coords[x, y]:
                        score_bottom += 1
                        break
                for other in left(x, y):
                    if coords[other] < coords[x, y]:
                        score_left += 1
                    if coords[other] >= coords[x, y]:
                        score_left += 1
                        break
                for other in right(x, y, n):
                    if coords[other] < coords[x, y]:
                        score_right += 1
                    if coords[other] >= coords[x, y]:
                        score_right += 1
                        break
                total = score_top * score_bottom * score_right * score_left
                if total > scenic_score:
                    scenic_score = total

    return scenic_score


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
