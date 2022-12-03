import argparse
import os
import pytest as pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_S = '''\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''


def compute(input_s: str) -> int:
    priority_sum = 0
    lines = input_s.strip().split('\n')
    for i in range(0, len(lines) - 2, 3):
        first, second, third = lines[i], lines[i + 1], lines[i + 2]
        first, second, third = set(first), set(second), set(third)
        priority = first.intersection(second, third)
        item = priority.pop()
        if 97 <= ord(item) <= 122:
            priority_sum += (ord(item) - 96)
        elif 65 <= ord(item) <= 90:
            priority_sum += (ord(item) - 38)

    return priority_sum


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
