import argparse
import os
from collections import deque
from copy import deepcopy

import pytest as pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_S = '''\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
'''


def compute(input_s: str):

    def bfs():
        deque_ = deque()
        for row in range(rows):
            for column in range(columns):
                if graph[row][column] == 'S':
                    deque_.append(((row, column), 0))
        set_ = set()
        while deque_:
            (r, c), s = deque_.popleft()
            if (r, c) in set_:
                continue
            set_.add((r, c))
            if graph[r][c] == 'E':
                return s
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < rows and 0 <= cc < columns and values[rr][cc] <= 1 + values[r][c]:
                    deque_.append(((rr, cc), s + 1))

    lines = input_s.strip().split('\n')
    graph = []
    for line in lines:
        graph.append(line)
    rows = len(graph)
    columns = len(graph[0])

    values = [[0 for _ in range(columns)] for _ in range(rows)]
    for row in range(rows):
        for column in range(columns):
            if graph[row][column] == 'S':
                values[row][column] = 1
            elif graph[row][column] == 'E':
                values[row][column] = 26
            else:
                values[row][column] = ord(graph[row][column]) - ord('a') + 1

    return bfs()


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
