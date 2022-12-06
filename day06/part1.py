import argparse
import os
from copy import deepcopy

import pytest as pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_S = '''\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
'''


def compute(input_s: str) -> int:
    value = 0
    data = input_s.strip()
    for i in range(len(data) - 3):
        marker = {data[i], data[i + 1], data[i + 2], data[i + 3]}
        if len(marker) == 4:
            value = i + 4
            return value

    return value


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
