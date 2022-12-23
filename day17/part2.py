import argparse
import os
from collections import defaultdict
from copy import deepcopy

import pytest as pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_S = '''\
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
'''


def compute(input_s: str):
    sensors = defaultdict(int)
    n = 4000000

    lines = input_s.strip().split('\n')
    for line in lines:
        first, second = line.split(':')
        sensor_x, sensor_y = first.split(',')
        beacon_x, beacon_y = second.split(',')
        s_x, s_y = int(sensor_x[12:]), int(sensor_y[3:])
        b_x, b_y = int(beacon_x[24:]), int(beacon_y[3:])

        dist = abs(s_x - b_x) + abs(s_y - b_y)
        sensors[(s_x, s_y)] = dist

    for r in range(n + 1):
        for c in range(n + 1):
            for sensor, distance in sensors.items():
                if abs(sensor[0] - c) + abs(sensor[1] - r) <= distance:
                    break
            else:
                print(f'x = {c} y = {r}')
                return c * 4000000 + r
        if r == 0:
            print('jestem')

    return 0


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
