# https://adventofcode.com/2021/day/10
import sys
from ..common import read_data
from collections import deque

open_chars = {"(", "[", "{", "<"}
open_close_mappings = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
corruption_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

def parse(data):
    inputs = []
    for line in data:
        inputs.append(list(line))
    return inputs

def corrupted_at(tokens):
    stack = deque()
    for token in tokens:
        if token in open_chars:
            stack.append(token)
            continue
        top = stack.pop()
        if open_close_mappings[top] != token:
            return token
    return None

def part1(data):
    inputs = parse(data)
    score = 0
    for i in inputs:
        corrupted_token = corrupted_at(i)
        if corrupted_token is not None:
            score += corruption_points[corrupted_token]
    return score



def part2(data):
    return ""


data = read_data(sys.argv[1], str)
print("-----------------------------------------------------------")
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")

