import argparse
import os
import pytest as pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_S = '''\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''

EXPECTED = 24000


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def compute(input_s: str) -> int:
    max_x = 0
    x = 0
    for line in input_s.split('\n'):
        if line != '':
            x += int(line)
        elif line == '':
            if x > max_x:
                max_x = x
                x = 0
            else:
                x = 0
    return max_x


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
