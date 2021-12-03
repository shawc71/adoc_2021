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
    return ""


data = read_data(sys.argv[1], int)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
