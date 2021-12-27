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
    min_char = None
    min_val = None
    for c in freq:
        if min_val is None or freq[c] < min_val:
            min_val = freq[c]
            min_char = c
    return min_val

def max_freq(freq):
    max_char = None
    max_val = None
    for c in freq:
        if max_val is None or freq[c] > max_val:
            max_val = freq[c]
            max_char = c
    return max_val

def part1(data):
    template, rules = parse(data)
    steps = 10
    for _ in range(steps):
        next_template = ""
        for idx, _ in enumerate(template):
            if idx <= len(template) - 2:
                pair = f"{template[idx]}{template[idx+1]}"
                if pair in rules:
                    insert = rules[pair]
                    if idx == 0:
                        to_append = f"{pair[0]}{insert}{pair[1]}"
                    else:
                        to_append = f"{insert}{pair[1]}"
                    next_template = f"{next_template}{to_append}"
        template = next_template
    freq = char_freq(template)
    return max_freq(freq) - min_freq(freq)

def part2(data):
    return ""


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")

