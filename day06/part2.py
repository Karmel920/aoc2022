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
    for i in range(len(data) - 13):
        marker = set(data[i:i+14])
        if len(marker) == 14:
            value = i + 14
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
