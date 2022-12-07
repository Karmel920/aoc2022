import pytest as pytest
from part1 import compute as compute1
from part2 import compute as compute2

INPUT_S = '''\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''

EXPECTED1 = 95437
EXPECTED2 = 24933642


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
