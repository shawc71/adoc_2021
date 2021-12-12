import sys
from ..common import read_data


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print(self):
        print(f"{self.start} -> {self.end}")

    def is_horizontal(self):
        return self.start[1] == self.end[1]

    def is_vertical(self):
        return self.start[0] == self.end[0]


def parse(data_lines):
    lines = []
    for data_line in data_lines:
        segment = data_line.split(" -> ")
        start_coords = segment[0].split(",")
        end_coords = segment[1].split(",")
        lines.append(Line((int(start_coords[0]), int(start_coords[1])), (int(end_coords[0]), int(end_coords[1]))))
    return lines


def part1(data):
    lines = parse(data)
    vents = build_part1_vent_map(lines)
    answer = 0
    for y in vents.keys():
        for x in vents[y].keys():
            if vents[y][x] > 1:
                answer += 1
    return answer


def build_part1_vent_map(lines):
    vents = {}
    for line in lines:
        if not (line.is_vertical() or line.is_horizontal()):
            continue
        if line.is_horizontal():
            y = line.start[1]
            start_x = line.start[0]
            end_x = line.end[0]
            if end_x < start_x:
                tmp = start_x
                start_x = end_x
                end_x = tmp
            x = start_x
            while x <= end_x:
                if y not in vents:
                    vents[y] = {}
                if x not in vents[y]:
                    vents[y][x] = 0
                vents[y][x] += 1
                x += 1
        elif line.is_vertical():
            x = line.start[0]
            start_y = line.start[1]
            end_y = line.end[1]
            if end_y < start_y:
                tmp = start_y
                start_y = end_y
                end_y = tmp
            y = start_y
            while y <= end_y:
                if y not in vents:
                    vents[y] = {}
                if x not in vents[y]:
                    vents[y][x] = 0
                vents[y][x] += 1
                y += 1
    return vents


def part2(data):
    return ""


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
