# https://adventofcode.com/2021/day/2
import sys
from ..common import read_data


def tokenize(movements):
    m = []
    for movement in movements:
        direction, value = movement.split(" ")
        m.append({
            'direction': direction,
            'value': int(value),
        })

    return m


def part1(data):
    horizontal = 0
    depth = 0
    for movement in tokenize(data):
        if movement['direction'] == 'forward':
            horizontal += movement['value']
        elif movement['direction'] == 'up':
            depth -= movement['value']
        elif movement['direction'] == 'down':
            depth += movement['value']
    return horizontal * depth


def part2(data):
    horizontal = 0
    depth = 0
    aim = 0
    for movement in tokenize(data):
        if movement['direction'] == 'forward':
            horizontal += movement['value']
            depth += (aim * movement['value'])
        elif movement['direction'] == 'up':
            aim -= movement['value']
        elif movement['direction'] == 'down':
            aim += movement['value']
    return horizontal * depth


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
