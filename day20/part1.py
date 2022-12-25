import argparse
import os
from collections import defaultdict
from collections import Counter
from copy import deepcopy
from tqdm import tqdm

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_S = '''\
1
2
-3
3
-2
0
4
'''


def compute(input_s: str) -> int:
    nums = []
    lines = input_s.strip().split('\n')
    for i, line in enumerate(lines):
        nums.append((i, int(line) * 811589153))

    n = len(nums)
    og = nums.copy()

    def swap(nums, a, b):
        assert (0 <= a < n) and (0 <= b < n)

        nums[a], nums[b] = nums[b], nums[a]
        return nums

    for i, x in og:
        for idx in range(n):
            if nums[idx][0] == i:
                break

        assert nums[idx][1] == x

        if x < 0:
            cur = idx
            for _ in range(-x):
                nums = swap(nums, cur, (cur - 1) % n)
                cur = (cur - 1) % n

            continue

        if x > 0:
            cur = idx
            for _ in range(x):
                nums = swap(nums, cur, (cur + 1) % n)
                cur = (cur + 1) % n

    coords = [1000, 2000, 3000]

    ans = 0
    for zero_idx in range(n):
        if nums[zero_idx][1] == 0:
            break

    for c in coords:
        ans += nums[(zero_idx + c) % n][1]

    return ans


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
