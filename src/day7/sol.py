import sys
from ..common import read_data

def parse(data):
    return sorted(list(map(lambda val: int(val), data.split(","))))


def calc_fuel(alignment_candidate, positions):
    total_fuel = 0
    for position in positions:
        total_fuel += abs(alignment_candidate - position)
    return total_fuel


def part1(data):
    positions = parse(data)
    alignment_candidate = positions[0]
    total_fuel = {}
    while alignment_candidate <= positions[-1]:
        total_fuel[alignment_candidate] = calc_fuel(alignment_candidate, positions)
        alignment_candidate += 1

    lowest = None
    for fuel in total_fuel.values():
        if lowest is None or fuel < lowest:
            lowest = fuel
    return lowest


def part2(data):
    return ""


data = read_data(sys.argv[1], str)[0]
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
