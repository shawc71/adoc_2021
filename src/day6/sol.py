# https://adventofcode.com/2021/day/6
import sys
from ..common import read_data
from collections import defaultdict


def process_round(timer_map):
    next_timer_map = defaultdict(lambda: 0)
    for fish_timer, freq in timer_map.items():
        if fish_timer == 0:
            next_timer_map[6] += freq
            next_timer_map[8] = freq
        else:
            next_timer_map[fish_timer - 1] += freq
    return next_timer_map


def part1(data, rounds):
    return part2(data, rounds)


def part2(data, rounds):
    timer_map = defaultdict(lambda: 0)
    for fish_timer in parse(data):
        timer_map[fish_timer] += 1
    for _ in range(rounds):
        timer_map = process_round(timer_map)
    count = 0
    for freq in timer_map.values():
        count += freq
    return count


def parse(line):
    return list(map(lambda x: int(x), line.split(",")))


data = read_data(sys.argv[1], str)[0]
rounds = int(sys.argv[2])
print(f"Part 1: {part1(data, rounds)}")
print(f"Part 2: {part2(data, rounds)}")
