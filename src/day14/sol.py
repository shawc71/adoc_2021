# https://adventofcode.com/2021/day/14
import sys
from ..common import read_data


def parse(data):
    PARSING_TEMPLATE = 0
    PARSING_RULES = 1
    state = PARSING_TEMPLATE
    template = ""
    rules = {}
    for line in data:
        line = line.strip()
        if line == "":
            state = PARSING_RULES
            continue
        if state == PARSING_TEMPLATE:
            template = line
        else:
            key, val = line.split(" -> ")
            rules[key] = val
    return template, rules


def char_freq(str):
    freq = {}
    for c in str:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1
    return freq


def min_freq(freq):
    min_val = None
    for c in freq:
        if min_val is None or freq[c] < min_val:
            min_val = freq[c]
    return min_val


def max_freq(freq):
    max_val = None
    for c in freq:
        if max_val is None or freq[c] > max_val:
            max_val = freq[c]
    return max_val


def increment_count_by(increment, histogram, *keys):
    for key in keys:
        if key not in histogram:
            histogram[key] = 0
        histogram[key] += increment


def increment_count(histogram, *keys):
    increment_count_by(1, histogram, *keys)


def solve(data, steps):
    template, rules = parse(data)
    pair_freqs = {}
    first_pair = None
    for idx, _ in enumerate(template):
        if idx <= len(template) - 2:
            pair = f"{template[idx]}{template[idx + 1]}"
            increment_count(pair_freqs, pair)
            if idx == 0:
                first_pair = pair
    counts = {}
    for step in range(steps):
        next_step_pair_freqs = {}
        for pair in pair_freqs:
            if pair not in rules:
                raise Exception("unexpected state")
            insert = rules[pair]
            if pair == first_pair:
                increment_count(counts, pair[0], insert, pair[1])
                increment_count_by(pair_freqs[pair] - 1, counts, insert, pair[1])
                first_pair = f"{pair[0]}{insert}"
            else:
                increment_count_by(pair_freqs[pair], counts, insert, pair[1])
            increment_count_by(pair_freqs[pair], next_step_pair_freqs, f"{pair[0]}{insert}", f"{insert}{pair[1]}")
        pair_freqs = next_step_pair_freqs
        if step != steps - 1:
            counts = {}
    return max_freq(counts) - min_freq(counts)


def part1(data):
    return solve(data, 10)


def part2(data):
    return solve(data, 40)


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
