# https://adventofcode.com/2021/day/10
import math
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

autocomplete_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
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


def autocomplete(tokens):
    stack = deque()
    for token in tokens:
        if token in open_chars:
            stack.append(token)
            continue
        top = stack.pop()
        assert open_close_mappings[top] == token
    if not stack:
        return []
    ret = []
    while len(stack) != 0:
        top = stack.pop()
        closing = open_close_mappings[top]
        ret.append(closing)
    return ret


def part1(data):
    inputs = parse(data)
    score = 0
    for i in inputs:
        corrupted_token = corrupted_at(i)
        if corrupted_token is not None:
            score += corruption_points[corrupted_token]
    return score


def part2(data):
    inputs = parse(data)
    scores = []
    for i in inputs:
        corrupted_token = corrupted_at(i)
        if corrupted_token is not None:
            continue
        score = 0
        for completion_token in autocomplete(i):
            score = (score * 5) + autocomplete_points[completion_token]
        scores.append(score)
    scores = sorted(scores)
    middle_idx = math.floor(len(scores)/2)
    return scores[middle_idx]


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
