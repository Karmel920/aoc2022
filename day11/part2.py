import argparse
import os

from tqdm import tqdm

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_S = '''\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
'''


class Monkey:

    def __init__(self, id_: int, items: list, operation: str, value: str, test_value: int, test_dict: dict):
        self.id_ = id_
        self.items = items
        self.operation = operation
        self.value = value
        self.test_value = test_value
        self.test_dict = test_dict
        self.counter = 0

    def new_wl(self, item) -> int:
        """return new worry_level of item"""
        self.counter += 1
        if self.value.isnumeric():
            if self.operation == '+':
                return item + int(self.value)
            elif self.operation == '*':
                return item * int(self.value)
        else:
            return item * item

    def get_monkey_to_throw(self, worry_level) -> int:
        """return id of monkey we're throwing to"""
        return self.test_dict[not bool(worry_level % self.test_value)]

    def append_item(self, item):
        self.items.append(item)

    def get_id_(self):
        return self.id_

    def is_not_empty(self):
        if len(self.items):
            return True
        return False

    def __str__(self):
        return f"Monkey {self.id_}: items={self.items}"


def compute(input_s: str):
    lines = input_s.strip().split('\n\n')
    monkeys = []
    for line in lines:
        m = line.strip().split('\n')
        id_ = int(m[0][7:-1])
        items = list(map(int, m[1].strip()[16:].split(', ')))
        operation = m[2].strip()[21:22]
        value = m[2].strip()[23:]
        test_value = int(m[3].strip()[19:])
        test_dict = {True: int(m[4].strip()[25:]),
                     False: int((m[5].strip()[26:]))}
        monkeys.append(Monkey(id_, items, operation, value, test_value, test_dict))

    for _ in tqdm(range(10000)):
        for i, monkey in enumerate(monkeys):
            if monkey.is_not_empty():
                for item in monkey.items:
                    worry_level = monkey.new_wl(item)
                    monkey_id_to_throw = monkey.get_monkey_to_throw(worry_level)
                    for throw_monkey in monkeys:
                        if throw_monkey.get_id_() == monkey_id_to_throw:
                            throw_monkey.items.append(worry_level)
                            break
                monkey.items = []
            else:
                continue

    ins_items = []
    for monkey in monkeys:
        # print(monkey)
        ins_items.append(monkey.counter)
    ins_items.sort(reverse=True)
    print(ins_items)

    return ins_items[0] * ins_items[1]


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
