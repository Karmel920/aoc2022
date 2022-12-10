import argparse
import os
from copy import deepcopy
from collections import defaultdict

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


def compute(input_s: str) -> int:
    lines = input_s.strip().split('\n')
    step = {'noop': 1, 'addx': 2}
    cycles = 0
    X = 1
    total_strength = 0
    for line in lines:
        if line == 'noop':
            cycles += 1
        else:
            instruction, value = line.split()
            value = int(value)
            cycles += 2
            if cycles % 40 == 20:
                X += value
                signal_strength = X * cycles
                total_strength += signal_strength
                print(f'Cycle {cycles}th, signal_strength = {signal_strength}, X = {X}')
            elif cycles % 40 == 21:
                signal_strength = X * (cycles - 1)
                total_strength += signal_strength
                print(f'Cycle {cycles - 1}th, signal_strength = {signal_strength}, X = {X}')
                X += value
            else:
                X += value
            continue
        if cycles % 40 == 20:
            signal_strength = X * cycles
            total_strength += signal_strength
            print(f'Cycle {cycles}th, signal_strength = {signal_strength}, X = {X}')

    return total_strength


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(INPUT_S))
        # print(compute(f.read()))

    return 0


if __name__ == '__main__':
    main()
