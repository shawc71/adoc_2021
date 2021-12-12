# https://adventofcode.com/2021/day/1
import sys

from ..common import read_data


def part1(data):
    increases = 0
    last = None
    for val in data:
        if last is None:
            last = val
            continue
        if val > last:
            increases += 1
        last = val
    return increases


def part2(data):
    increases = 0
    last_window = None

    for i, val in enumerate(data):
        if last_window is None and len(data) > i + 2:
            last_window = data[i] + data[i + 1] + data[i + 2]
            continue
        if len(data) <= i + 2:
            break

        curr_window = data[i] + data[i + 1] + data[i + 2]
        if curr_window > last_window:
            increases += 1
        last_window = curr_window
    return increases


data = read_data(sys.argv[1], int)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
