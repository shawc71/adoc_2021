# https://adventofcode.com/2021/day/16
import sys
from ..common import *

PACKET_TYPE_LITERAL = 4


class Packet:
    def __init__(self, version, type_id, val):
        self.version = version
        self.type_id = type_id
        self.val = val
        self.subpackets = []

    def add_subpacket(self, packet):
        self.subpackets.append(packet)

    def cumulative_version_sum(self):
        if len(self.subpackets) == 0:
            return self.version
        version_sum = self.version
        for s in self.subpackets:
            version_sum += s.cumulative_version_sum()
        return version_sum


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
    version = int(data[0:3], 2)
    type_id = int(data[3:6], 2)
    number = ""
    for start in range(6, len(data), 5):
        end = start + 5
        number += data[start + 1: end]
        if data[start] == "0":
            val = int(number, 2)
            packet = Packet(version, type_id, val)
            return packet, end
    raise Exception("illegal state")


def parse_sub_packets_by_bitcount(data):
    version = int(data[0:3], 2)
    type_id = int(data[3:6], 2)
    total_sub_packet_bits = int(data[7:22], 2)
    payload = data[22:]
    next_packet_start = 0
    consumed_bits = 0
    packet = Packet(version, type_id, None)
    while consumed_bits < total_sub_packet_bits:
        payload = payload[next_packet_start:]
        subpacket, next_packet_start = parse_packet(payload)
        packet.add_subpacket(subpacket)
        consumed_bits += next_packet_start
    return packet, 22 + total_sub_packet_bits


def parse_sub_packets_by_packet_count(data):
    version = int(data[0:3], 2)
    type_id = int(data[3:6], 2)
    total_packets = int(data[7:18], 2)
    next_packet_start = 0
    payload = data[18:]
    consumed_bits = 0
    packet = Packet(version, type_id, None)
    for i in range(total_packets):
        payload = payload[next_packet_start:]
        subpacket, next_packet_start = parse_packet(payload)
        packet.add_subpacket(subpacket)
        consumed_bits += next_packet_start
    return packet, 18 + consumed_bits


def parse_operator_packet(data):
    length_type_id = data[6]
    if length_type_id == "0":
        return parse_sub_packets_by_bitcount(data)
    else:
        return parse_sub_packets_by_packet_count(data)


def parse_packet(payload):
    type_id = payload[3:6]
    if int(type_id, 2) == PACKET_TYPE_LITERAL:
        return parse_literal_value(payload)
    return parse_operator_packet(payload)


def process(data):
    payload = to_binary(data)
    return parse_packet(payload)


def part1(data):
    packet, _ = process(data)
    return packet.cumulative_version_sum()


def part2(data):
    return ""


data = read_data(sys.argv[1], str)
data = "".join(data)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
