# https://adventofcode.com/2021/day/18
import sys
from collections import deque
from ..common import *

class SnailfishNumber:
    def __init__(self, left=None, right=None, val=None):
        self.left = left
        self.right = right
        self.val = val

    def __repr__(self):
        if self.val is not None:
            return str(self.val)
        text = "[" + self.left.__repr__() + "," + self.right.__repr__() + "]"
        return text

def parse_number(line):
    stack = deque()
    for char in line:
        if char == ",":
            continue
        if char == '[':
            stack.append(char)
        elif char.isdigit():
            stack.append(SnailfishNumber(val=int(char)))
        elif char == "]":
            right = stack.pop()
            left = stack.pop()
            assert "[" == stack.pop()
            stack.append(SnailfishNumber(left=left, right=right))
        else:
            raise Exception(f"unexpected character <{char}>")

    assert len(stack) == 1
    return stack.pop()

def parse(data):
    numbers = []
    for line in data:
        numbers.append(parse_number(line))
    for n in numbers:
        print(n)
    return numbers

def part1(data):
    parse(data)
    return ""


def part2(data):
    return ""


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")

