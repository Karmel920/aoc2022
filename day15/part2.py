import argparse
import os
from tqdm import tqdm

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


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def compute(input_s: str):
    sensors = []
    beacons = []

    lines = input_s.strip().split('\n')
    for line in lines:
        parts = line.split()
        s_x, s_y = int(parts[2][2:-1]), int(parts[3][2:-1])
        b_x, b_y = int(parts[8][2:-1]), int(parts[9][2:])

        sensors.append((s_x, s_y))
        beacons.append((b_x, b_y))

    N = len(sensors)
    dists = []

    for i in range(N):
        dists.append(dist(sensors[i], beacons[i]))

    pos_lines = []
    neg_lines = []

    for i, s in enumerate(sensors):
        d = dists[i]
        neg_lines.extend([s[0] + s[1] - d, s[0] + s[1] + d])
        pos_lines.extend([s[0] - s[1] - d, s[0] - s[1] + d])

    pos = None
    neg = None

    for i in range(2 * N):
        for j in range(i + 1, 2 * N):
            a, b = pos_lines[i], pos_lines[j]

            if abs(a - b) == 2:
                pos = min(a, b) + 1

            a, b = neg_lines[i], neg_lines[j]

            if abs(a - b) == 2:
                neg = min(a, b) + 1

    x, y = (pos + neg) // 2, (neg - pos) // 2
    print(x, y)
    return x * 4000000 + y


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
