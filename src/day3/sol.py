import sys
from ..common import read_data


def most_common(freq):
    if freq['0'] > freq['1']:
        return '0'
    else:
        return '1'


def least_common(freq):
    if freq['1'] < freq['0']:
        return '1'
    else:
        return '0'


def calc_bit_freqs(bin_numbers):
    bits_per_number = len(bin_numbers[0])
    bit_frequencies = [{} for _ in range(bits_per_number)]
    for binary_number in bin_numbers:
        for bit_position, bit in enumerate(binary_number):
            if bit not in bit_frequencies[bit_position]:
                bit_frequencies[bit_position][bit] = 0
            bit_frequencies[bit_position][bit] += 1
    return bit_frequencies


def part1(bin_numbers):
    gamma = ""
    epsilon = ""
    bit_frequencies = calc_bit_freqs(bin_numbers)

    for freq in bit_frequencies:
        gamma += most_common(freq)
        epsilon += least_common(freq)

    return int(gamma, 2) * int(epsilon, 2)


def calc_rating(candidates, most_or_least_common_func):
    rating = None
    idx = 0
    max_ids = len(candidates[0])
    while rating is None and idx < max_ids:
        freq = calc_bit_freqs(candidates)
        target_bit = most_or_least_common_func(freq[idx])
        candidates = list(filter(lambda curr: curr[idx] == target_bit, candidates))
        if len(candidates) == 1:
            rating = candidates[0]
        idx += 1
    return int(rating, 2)


def part2(bin_numbers):
    o2_rating = calc_rating(bin_numbers, most_common)
    co2_rating = calc_rating(bin_numbers, least_common)
    return o2_rating * co2_rating


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
