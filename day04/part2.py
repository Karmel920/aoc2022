import argparse
import os
import pytest as pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_S = '''\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''


def compute(input_s: str) -> int:
    pairs = 0
    for line in input_s.strip().split('\n'):
        pair1, pair2 = line.split(',')
        low1, high1 = pair1.split('-')
        low2, high2 = pair2.split('-')
        set_p1 = {n for n in range(int(low1), int(high1) + 1)}
        set_p2 = {n for n in range(int(low2), int(high2) + 1)}
        if set_p1.intersection(set_p2):
            pairs += 1

    return pairs


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
