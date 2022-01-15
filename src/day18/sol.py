# https://adventofcode.com/2021/day/18
import math
import sys
from collections import deque
from ..common import *


class SnailfishNumber:
    def __init__(self, left=None, right=None, parent=None, val=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.val = val

    def __repr__(self):
        if self.val is not None:
            return str(self.val)
        text = "[" + self.left.__repr__() + "," + self.right.__repr__() + "]"
        return text

    def add(self, other):
        root_node = SnailfishNumber(left=self, right=other)
        self.parent = root_node
        other.parent = root_node
        has_changes = True
        while has_changes:
            # print(root_node)
            has_changes = False
            explosion_candidate = root_node.get_explosion_candidate()
            print(explosion_candidate)
            if explosion_candidate is not None:
                # print(f"candidate: {explosion_candidate}")
                explosion_candidate.explode()
                has_changes = True
                continue

            split_candidates = root_node.get_split_candidate()
            # print(f"splt: {split_candidate}")
            if len(split_candidates) != 0:
                # print(split_candidates)
                split_candidates[0].split()
                has_changes = True

        return root_node

    def reduce(self):
        changes = 0
        explosion_candidate = self.get_explosion_candidate()
        if explosion_candidate is None:
            return
        print(f"candidate: {explosion_candidate}")
        changes += 1
        explosion_candidate.explode()
        # print(f"post: {n}")
    
        split_candidates = self.get_split_candidate()
        # print(f"splt: {split_candidate}")
        if len(split_candidates) == 0:
            break
        changes += 1
        split_candidates[0].split()
        # print(f"post: {n}")
        return changes

    def split(self):
        left_val = math.floor(self.val/2)
        right_val = math.ceil(self.val/2)
        left_node = SnailfishNumber(val=left_val, parent=self)
        right_node = SnailfishNumber(val=right_val, parent=self)
        self.left = left_node
        self.right = right_node
        self.val = None

    def explode(self):
        if self.left is not None:
            left_val = self.left.val
            self._distribute_left(left_val, self)
        if self.right is not None:
            right_val = self.right.val
            self._distribute_right(right_val, self)
        self.val = 0
        self.left = None
        self.right = None

    def get_explosion_candidate(self):
        return SnailfishNumber._explosion_candidate_helper(0, self)

    def get_split_candidate(self):
        return SnailfishNumber._split_candidate_helper(self)

    @staticmethod
    def _distribute_left(val, curr_node):
        if curr_node.parent is None:
            return
        if curr_node.parent.left is not None and curr_node.parent.left != curr_node:
            if curr_node.parent.left.right is None:
                # print(curr_node.parent.left.val, val)
                curr_node.parent.left.val += val
                return
            curr_node = curr_node.parent.left.right
            while curr_node.right is not None:
                curr_node = curr_node.right
            curr_node.val += val
        return SnailfishNumber._distribute_left(val, curr_node.parent)

    @staticmethod
    def _distribute_right(val, curr_node):
        if curr_node.parent is None:
            return
        if curr_node.parent.right is not None and curr_node.parent.right != curr_node:
            if curr_node.parent.right.left is None:
                curr_node.parent.right.val += val
                return
            curr_node = curr_node.parent.right.left
            while curr_node.left is not None:
                curr_node = curr_node.left
            curr_node.val += val
            return
        return SnailfishNumber._distribute_right(val, curr_node.parent)

    @staticmethod
    def _explosion_candidate_helper(level, node):
        if level == 4 and node.left is not None and node.right is not None:
            return node

        next_level = level + 1
        if node.left is not None:
            candidate = SnailfishNumber._explosion_candidate_helper(next_level, node.left)
            if candidate is not None:
                return candidate

        if node.right is not None:
            candidate = SnailfishNumber._explosion_candidate_helper(next_level, node.right)
            if candidate is not None:
                return candidate

        return None

    @staticmethod
    def _split_candidate_helper(node):
        # print(node)
        to_return = []
        if node.val is not None and node.val >= 10:
            return [node]
        if node.left is not None:
            to_return.extend(SnailfishNumber._split_candidate_helper(node.left))
        if node.right is not None:
            to_return.extend(SnailfishNumber._split_candidate_helper(node.right))
        return to_return

def parse_number(line):
    stack = deque()
    for char in line:
        if char == ",":
            continue
        if char == '[':
            stack.append(char)
        elif char.isdigit():
            # if char == "!":
            #     char = "15"
            # if char == "@":
            #     char = "13"
            stack.append(SnailfishNumber(val=int(char)))
        elif char == "]":
            right = stack.pop()
            left = stack.pop()
            new_node = SnailfishNumber(left=left, right=right)
            right.parent = new_node
            left.parent = new_node
            assert "[" == stack.pop()
            stack.append(new_node)
        else:
            raise Exception(f"unexpected character <{char}>")

    assert len(stack) == 1
    return stack.pop()


def parse(data):
    numbers = []
    for line in data:
        numbers.append(parse_number(line))
    # for n in numbers:
    #     print(n)
    return numbers


def part1(data):
    numbers = parse(data)
    curr_sum = numbers[0]
    for i in range(1, len(numbers)):
        curr_sum = curr_sum.add(numbers[i])
        # print(curr_sum)
    return ""


def part2(data):
    return ""


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
