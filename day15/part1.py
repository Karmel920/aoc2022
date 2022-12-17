import argparse
import os
from collections import defaultdict

import pytest as pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_S = '''\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
'''


def compute(input_s: str):
    sensors = set()
    beacons = set()
    nb = set()
    n_row = 2000000

    lines = input_s.strip().split('\n')
    for line in lines:
        first, second = line.split(':')
        sensor_x, sensor_y = first.split(',')
        beacon_x, beacon_y = second.split(',')
        s_x, s_y = int(sensor_x[12:]), int(sensor_y[3:])
        b_x, b_y = int(beacon_x[24:]), int(beacon_y[3:])
        sensors.add((s_x, s_y))
        beacons.add((b_x, b_y))

        dist = abs(s_x - b_x) + abs(s_y - b_y)

        if s_y > n_row:
            diff = s_y - dist
            if diff < n_row:
                for c in range(0, dist - (s_y - n_row) + 1):
                    nb.add((s_x + c, n_row))
                    nb.add((s_x - c, n_row))
            elif diff == n_row:
                nb.add((s_x, diff))
        elif s_y < n_row:
            diff = s_y + dist
            if diff > n_row:
                for c in range(0, dist - (n_row - s_y) + 1):
                    nb.add((s_x + c, n_row))
                    nb.add((s_x - c, n_row))
            elif diff == n_row:
                nb.add((s_x, diff))
        elif s_y == n_row:
            for c in range(0, dist + 1):
                nb.add((s_x + c, n_row))
                nb.add((s_x - c, n_row))


        # for r in range(dist + 1):
        #     for c in range(0, dist - r + 1):
        #         if s_y + r == 10:
        #             nb.add((s_x + c, s_y + r))
        #             nb.add((s_x - c, s_y + r))
        #         if s_y - r == 10:
        #             nb.add((s_x + c, s_y - r))
        #             nb.add((s_x - c, s_y - r))

    return len(nb.difference(beacons))



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
