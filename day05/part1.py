import argparse
import os
from copy import deepcopy

import pytest as pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_S = '''\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''


def compute(input_s: str) -> str:
    lines = input_s.split('\n')
    stacks = []
    for line in lines:
        if line == '':
            break

        stacks_number = (len(line) + 1) // 4
        while len(stacks) < stacks_number:
            stacks.append([])

        for i in range(len(stacks)):
            crate = line[1 + 4 * i]
            if crate != ' ' and 'A' <= crate <= 'Z':
                stacks[i].append(crate)
    # print(stacks)

    found = False
    for line in lines:
        if line == '':
            found = True
            continue
        if not found:
            continue
        instruction = line.split()
        quantity = int(instruction[1])
        from_ = int(instruction[3]) - 1
        to_ = int(instruction[5]) - 1

        move = stacks[from_][:quantity]
        move_copy = deepcopy(move)
        move_copy.reverse()
        # print(move_copy)

        stacks[from_] = stacks[from_][quantity:]
        to_copy = deepcopy(stacks[to_])
        stacks[to_] = move_copy
        for crate in to_copy:
            stacks[to_].append(crate)
        # print(stacks)

    return ''.join([s[0] for s in stacks if len(s) > 0])


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
