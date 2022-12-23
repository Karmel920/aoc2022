import argparse
import os
from collections import defaultdict

import pytest as pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_S = '''\
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
'''

matrix = [[0,  1,   2,  3],
          [4,  5,   6,  7],
          [8,  9,  10, 11],
          [12, 13, 14, 15]]


class Figure:
    figures = [[0, 1, 2, 3],
               [1, 4, 5, 6, 9],
               [2, 6, 8, 9, 10],
               [0, 4, 8, 12],
               [0, 1, 4, 5]]

    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.type = n

    def image(self):
        return self.figures[self.type]


class Chamber:
    field = []
    height = 3
    width = 7
    iterations = 2
    it = 0
    jet_pattern = ''
    typ = 0
    tall = 0
    figure = None

    def __init__(self, jet_pattern):
        self.jet_pattern = jet_pattern
        for i in range(self.height):
            new_line = []
            for j in range(self.width):
                new_line.append(0)
            self.field.append(new_line)

    def new_figure(self, x, y, n):
        self.figure = Figure(x, y, n)

    def intersects_x(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if j + self.figure.x > self.width - 1 or j + self.figure.x < 0 or self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection

    def intersects_y(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = 1
        self.typ += 1
        self.typ = self.typ % 5
        self.height += self.get_new_height()
        self.it += 1
        self.new_figure(2, 0, self.typ)

    def go_down(self):
        self.figure.y += 1
        if self.intersects_y():
            self.figure.y -= 1
            self.freeze()

    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects_x():
            self.figure.x = old_x

    def get_new_height(self):
        diff = 0
        for i in range(self.height-1, -1, -1):
            if 1 in self.field[i]:
                diff += 1
            else:
                break
        tmp = diff - self.tall
        self.tall = diff
        for row in range(tmp):
            new_line = []
            for j in range(self.width):
                new_line.append(0)
            self.field.insert(0, new_line)
        return tmp

    def game(self):
        s = 0
        self.new_figure(2, 0, self.typ)
        print(self.field)
        print(self.figure.x, self.figure.y)
        while self.it < self.iterations:
            direction = self.jet_pattern[s % len(self.jet_pattern)]
            if direction == '>':
                self.go_side(1)
            elif direction == '<':
                self.go_side(-1)
            self.go_down()
            print(self.figure.x, self.figure.y)
        print(self.field)
        return self.tall, self.height


def compute(input_s: str):
    jet_pattern = input_s.strip()
    chamber = Chamber(jet_pattern)
    return chamber.game()


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
