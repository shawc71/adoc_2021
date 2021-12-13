# https://adventofcode.com/2021/day/8
import sys
from ..common import read_data

mapping_by_segment_count = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}
unique_segment_counts = {2, 4, 3, 7}


def parse(data):
    input = []
    for line in data:
        patterns, output = line.split(" | ")
        patterns = list(map(lambda word: "".join(sorted(word)), patterns.split()))
        output = list(map(lambda word: "".join(sorted(word)), output.split()))

        input.append({
            'signal_patterns': patterns,
            'output': output,
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


def difference(first, second):
    return len(set(first).difference(set(second)))


def intersection(first, second):
    return len(set(first).intersection(set(second)))


def part2(data):
    encodings = {}
    inputs = parse(data)
    totals = 0
    for input in inputs:
        for pattern in input['signal_patterns']:
            if len(pattern) in mapping_by_segment_count:
                encodings[mapping_by_segment_count[len(pattern)]] = pattern

        for pattern in input['signal_patterns']:
            if len(pattern) == 5:
                if difference(pattern, encodings[1]) == 3:
                    encodings[3] = pattern
                elif difference(pattern, encodings[4]) == 3:
                    encodings[2] = pattern
                else:
                    encodings[5] = pattern
            elif len(pattern) == 6:
                if intersection(encodings[4], pattern) == 4:
                    encodings[9] = pattern
                elif intersection(encodings[1], pattern) == 1:
                    encodings[6] = pattern
                else:
                    encodings[0] = pattern
        pattern_to_encoding_map = {}
        for k, v in encodings.items():
            pattern_to_encoding_map[v] = k

        num = ""
        for output in input['output']:
            num += str(pattern_to_encoding_map[output])
        totals += int(num)
    return totals


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
