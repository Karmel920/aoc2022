import argparse
import os
import pytest as pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(input_s: str) -> int:
    max_list = []
    x = 0
    for line in input_s.split('\n'):
        if line != '':
            x += int(line)
        elif line == '':
            max_list.append(x)
            x = 0

    max_list.sort(reverse=True)
    return sum(max_list[:3])


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
