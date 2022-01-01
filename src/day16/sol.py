# https://adventofcode.com/2021/day/16
import sys
from ..common import *


class Packet:
    def __init__(self):
        pass


PACKET_TYPE_LITERAL = 4
version_sum = 0

def to_binary(target):
    mappings = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    result = ""
    for t in target:
        result = f"{result}{mappings[t]}"
    return result


def parse_literal_value(data):
    number = ""
    for start in range(0, len(data), 5):
        end = start + 5
        number += data[start + 1: end]
        if data[start] == "0":
            val = int(number, 2)
            return end
    raise Exception("illegal state")


def parse_sub_packets_by_bitcount(data):
    total_sub_packet_bits = int(data[0:15], 2)
    payload = data[15:]
    next_packet_start = 0
    consumed_bits = 0
    while consumed_bits < total_sub_packet_bits:
        payload = payload[next_packet_start:]
        next_packet_start = parse_packet(payload)
        consumed_bits += next_packet_start
    return 15 + total_sub_packet_bits

def parse_sub_packets_by_packet_count(data):
    total_packets = int(data[0:11], 2)
    next_packet_start = 0
    payload = data[11:]
    consumed_bits = 0
    for i in range(total_packets):
        payload = payload[next_packet_start:]
        next_packet_start = parse_packet(payload)
        consumed_bits += next_packet_start
    return 11 + consumed_bits

def parse_operator_packet(data):
    length_type_id = data[0]
    if length_type_id == "0":
        return 1 + parse_sub_packets_by_bitcount(data[1:])
    else:
        return 1 + parse_sub_packets_by_packet_count(data[1:])

def parse_packet(payload):
    global version_sum
    version = payload[0:3]
    version_sum += int(version, 2)
    type_id = payload[3:6]
    if int(type_id, 2) == PACKET_TYPE_LITERAL:
        return 6 + parse_literal_value(payload[6:])
    else:
        return 6 + parse_operator_packet(payload[6:])


def process(data):
    payload = to_binary(data)
    parse_packet(payload)



def part1(data):
    process(data)
    global version_sum
    return version_sum


def part2(data):
    return ""


data = read_data(sys.argv[1], str)
data = "".join(data)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
