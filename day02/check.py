import pytest as pytest
from part1 import compute as compute1
from part2 import compute as compute2

INPUT_S = '''\
A Y
B X
C Z
'''

EXPECTED1 = 15
EXPECTED2 = 12


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            (INPUT_S, EXPECTED1),
    ),
)
def test1(input_s: str, expected: int) -> None:
    assert compute1(input_s) == expected


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            (INPUT_S, EXPECTED2),
    ),
)
def test2(input_s: str, expected: int) -> None:
    assert compute2(input_s) == expected
