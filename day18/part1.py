import argparse
import os
import numpy as np

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_S = '''\
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
'''


def compute(input_s: str) -> int:
    cubes = set()
    lines = input_s.strip().split('\n')
    for line in lines:
        x, y, z = map(int, line.split(','))
        cubes.add((x, y, z))

    total = 0
    for x, y, z in cubes:
        covered = 0
        pos = np.array((x, y, z))
        for i in range(3):
            dpositive = np.array([0, 0, 0])
            dpositive[i] = 1
            dnegative = np.array([0, 0, 0])
            dnegative[i] = -1

            covered += tuple(pos + dpositive) in cubes
            covered += tuple(pos + dnegative) in cubes
        total += 6 - covered
    return total


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
