import sys
from ..common import read_data


def most_common(freq):
    if freq['0'] > freq['1']:
        return '0'
    else:
        return '1'

def least_common(freq):
    if freq['0'] < freq['1']:
        return '0'
    else:
        return '1'

def part1(bin_numbers):
    gamma = ""
    epsilon = ""
    bits_per_number = len(bin_numbers[0])
    bit_frequencies = [{} for _ in range(bits_per_number)]
    for binary_number in bin_numbers:
        for bit_position, bit in enumerate(binary_number):
            if bit not in bit_frequencies[bit_position]:
                bit_frequencies[bit_position][bit] = 0
            bit_frequencies[bit_position][bit] += 1

    for freq in bit_frequencies:
        gamma += most_common(freq)
        epsilon += least_common(freq)

    return int(gamma, 2) * int(epsilon, 2)


def part2(data):
    return ""


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
