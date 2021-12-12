import sys
from ..common import read_data


def process_round(state):
    next_state = []
    for fish_timer in state:
        if fish_timer == 0:
            next_state.append(6)
            next_state.append(8)
        else:
            next_state.append(fish_timer - 1)
    return next_state


def part1(data, rounds):
    state = parse(data)
    for _ in range(rounds):
        state = process_round(state)
    return len(state)


def part2(data, rounds):
    return ""


def parse(line):
    return list(map(lambda x: int(x), line.split(",")))


data = read_data(sys.argv[1], str)[0]
rounds = int(sys.argv[2])
print(f"Part 1: {part1(data, rounds)}")
print(f"Part 2: {part2(data, rounds)}")
