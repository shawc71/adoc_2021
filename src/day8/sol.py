# https://adventofcode.com/2021/day/8
import sys
from ..common import read_data

segment_counts = {
    1: 2,
    4: 4,
    7: 3,
    8: 7,
}
unique_segment_counts = {2, 4, 3, 7}
def parse(data):
    input = []
    for line in data:
        patterns, output = line.split(" | ")
        input.append({
            'signal_patterns': patterns.split(),
            'output': output.split(),
        })
    return input

def part1(data):
    inputs = parse(data)
    total = 0
    for input in inputs:
        for digit_representation in input['output']:
            segments_used = len(digit_representation)
            if segments_used in unique_segment_counts:
                total += 1
    return total


def part2(data):
    return ""


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")

