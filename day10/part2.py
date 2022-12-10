import argparse
import os
from collections import defaultdict
from copy import deepcopy

import pytest as pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_S = '''\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
'''


def compute(input_s: str):
    lines = input_s.strip().split('\n')
    CRT = []
    cycles = 0
    X = 1
    image = ''
    for line in lines:
        if line == 'noop':
            cycles += 1
            if (cycles + len(CRT)) % 41 == 0 and cycles >= 40:
                CRT.append(image)
                image = ''
            if ((cycles - 1) % 40) in (X - 1, X, X + 1):
                image += '#'
            else:
                image += ' '
        else:
            instruction, value = line.split()
            value = int(value)
            cycles += 1
            if (cycles + len(CRT)) % 41 == 0 and cycles >= 40:
                CRT.append(image)
                image = ''
            if ((cycles - 1) % 40) in (X - 1, X, X + 1):
                image += '#'
            else:
                image += ' '
            cycles += 1
            if (cycles + len(CRT)) % 41 == 0 and cycles >= 40:
                CRT.append(image)
                image = ''
            if ((cycles - 1) % 40) in (X - 1, X, X + 1):
                image += '#'
            else:
                image += ' '
            X += value
        if cycles == 240:
            CRT.append(image)

    for line in CRT:
        print(line, len(line))



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
