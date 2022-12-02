import argparse
import os
import pytest as pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_S = '''\
A Y
B X
C Z
'''


def compute(input_s: str) -> int:
    total_score = 0
    for line in input_s.strip().split('\n'):
        player1, player2 = line.split()
        if player2 == 'X':
            if player1 == 'A':
                total_score += 3
            elif player1 == 'B':
                total_score += 1
            elif player1 == 'C':
                total_score += 2
        elif player2 == 'Y':
            total_score += 3
            if player1 == 'A':
                total_score += 1
            elif player1 == 'B':
                total_score += 2
            elif player1 == 'C':
                total_score += 3
        elif player2 == 'Z':
            total_score += 6
            if player1 == 'A':
                total_score += 2
            elif player1 == 'B':
                total_score += 3
            elif player1 == 'C':
                total_score += 1

    return total_score


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
