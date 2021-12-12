import sys
from ..common import read_data


def parse(data):
    return sorted(list(map(lambda val: int(val), data.split(","))))


def calc_fuel(alignment_candidate, positions):
    total_fuel = 0
    for position in positions:
        total_fuel += abs(alignment_candidate - position)
    return total_fuel


def calc_fuel_part_2(alignment_candidate, positions):
    total_fuel = 0
    for position in positions:
        no_of_moves = abs(alignment_candidate - position)
        total_fuel += (no_of_moves * (no_of_moves + 1)) / 2
    return total_fuel


def solve(data, fuel_calc_func):
    positions = parse(data)
    alignment_candidate = positions[0]
    total_fuel = {}
    while alignment_candidate <= positions[-1]:
        total_fuel[alignment_candidate] = fuel_calc_func(alignment_candidate, positions)
        alignment_candidate += 1

    lowest = None
    for fuel in total_fuel.values():
        if lowest is None or fuel < lowest:
            lowest = fuel
    return lowest


def part1(data):
    return solve(data, calc_fuel)


def part2(data):
    return solve(data, calc_fuel_part_2)


data = read_data(sys.argv[1], str)[0]
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
