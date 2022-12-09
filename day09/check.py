import pytest as pytest
from part1 import compute as compute1
from part2 import compute as compute2

INPUT_S = '''\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''

INPUT_S2 = '''\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
'''

EXPECTED1 = 13
EXPECTED2 = 36


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
            (INPUT_S2, EXPECTED2),
    ),
)
def test2(input_s: str, expected: int) -> None:
    assert compute2(input_s) == expected
