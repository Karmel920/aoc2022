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
        pair1_low, pair1_high = pair1.split('-')
        pair2_low, pair2_high = pair2.split('-')
        if int(pair1_low) <= int(pair2_low):
            if int(pair1_high) >= int(pair2_high):
                pairs += 1
                continue
        if int(pair1_low) >= int(pair2_low):
            if int(pair1_high) <= int(pair2_high):
                pairs += 1
                continue
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
