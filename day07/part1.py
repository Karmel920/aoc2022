import argparse
import os
from copy import deepcopy
from collections import defaultdict

import pytest as pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

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


def compute(input_s: str) -> int:
    sizes = defaultdict(int)
    path = []
    sum_ = 0
    lines = input_s.strip().split('\n')
    for line in lines:
        words = line.strip().split()

        if words[1] == 'cd':
            if words[2] == '..':
                path.pop()
            else:
                path.append(words[2])
        elif words[1] == 'ls':
            continue
        elif words[0] == 'dir':
            continue
        else:
            size = int(words[0])
            for i in range(1, len(path) + 1):
                sizes['/'.join(path[:i])] += size

    for k, v in sizes.items():
        if v <= 100000:
            sum_ += v
        print(k, v)

    return sum_


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(INPUT_S))
        # print(compute(f.read()))

    return 0


if __name__ == '__main__':
    main()
