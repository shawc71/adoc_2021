# https://adventofcode.com/2021/day/5
import sys
from ..common import read_data


class Line:
    TOP_LEFT = 0
    TOP_RIGHT = 1
    BOTTOM_LEFT = 2
    BOTTOM_RIGHT = 3

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.is_diagonal = False
        self.orientation = None
        self.calc_diagonal()

    def is_horizontal(self):
        return self.start[1] == self.end[1]

    def is_vertical(self):
        return self.start[0] == self.end[0]

    def get_points(self):
        if self.is_horizontal():
            return self.get_horizontal_points()
        elif self.is_vertical():
            return self.get_vertical_points()
        else:
            return self.get_diagonal_points()

    def get_horizontal_points(self):
        if not self.is_horizontal():
            return []
        points = []
        y = self.start[1]
        start_x = self.start[0]
        end_x = self.end[0]
        if end_x < start_x:
            tmp = start_x
            start_x = end_x
            end_x = tmp
        x = start_x
        while x <= end_x:
            points.append((x, y))
            x += 1
        return points

    def get_vertical_points(self):
        if not self.is_vertical():
            return []
        points = []
        x = self.start[0]
        start_y = self.start[1]
        end_y = self.end[1]
        if end_y < start_y:
            tmp = start_y
            start_y = end_y
            end_y = tmp
        y = start_y
        while y <= end_y:
            points.append((x, y))
            y += 1
        return points

    def get_diagonal_points(self):
        if not self.is_diagonal:
            return []
        points = []
        y = self.start[0]
        x = self.start[1]
        if self.orientation == self.TOP_LEFT:
            while y >= self.end[0] and x >= self.end[1]:
                points.append((y, x))
                y -= 1
                x -= 1
        elif self.orientation == self.TOP_RIGHT:
            while y >= self.end[0] and x <= self.end[1]:
                points.append((y, x))
                y -= 1
                x += 1
        elif self.orientation == self.BOTTOM_RIGHT:
            while y <= self.end[0] and x <= self.end[1]:
                points.append((y, x))
                y += 1
                x += 1
        else:
            while y <= self.end[0] and x >= self.end[1]:
                points.append((y, x))
                y += 1
                x -= 1
        return points

    def calc_diagonal(self):
        if self.is_horizontal() or self.is_vertical():
            return
        if self.start[0] > self.end[0] and self.start[1] > self.end[1]:
            y = self.start[0]
            x = self.start[1]
            while y >= self.end[0] and x >= self.end[1]:
                if self.end[0] == y and self.end[1] == x:
                    self.orientation = self.TOP_LEFT
                    self.is_diagonal = True
                    return
                y -= 1
                x -= 1

        elif self.start[0] > self.end[0] and self.start[1] < self.end[1]:
            y = self.start[0]
            x = self.start[1]
            while y >= self.end[0] and x <= self.end[1]:
                if self.end[0] == y and self.end[1] == x:
                    self.orientation = self.TOP_RIGHT
                    self.is_diagonal = True
                    return
                y -= 1
                x += 1

        elif self.start[0] < self.end[0] and self.start[1] < self.end[1]:
            y = self.start[0]
            x = self.start[1]
            while y <= self.end[0] and x <= self.end[1]:
                if self.end[0] == y and self.end[1] == x:
                    self.orientation = self.BOTTOM_RIGHT
                    self.is_diagonal = True
                    return
                y += 1
                x += 1
        else:
            y = self.start[0]
            x = self.start[1]
            while y <= self.end[0] and x >= self.end[1]:
                if self.end[0] == y and self.end[1] == x:
                    self.orientation = self.BOTTOM_LEFT
                    self.is_diagonal = True
                    return
                y += 1
                x -= 1


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
    vents = {}
    add_vertical_horizontal_lines(vents, lines)
    return count_intersections(vents)


def part2(data):
    lines = parse(data)
    vents = {}
    add_vertical_horizontal_lines(vents, lines)
    add_diagonals(lines, vents)
    return count_intersections(vents)


def add_vertical_horizontal_lines(vents, lines):
    for line in lines:
        if not (line.is_vertical() or line.is_horizontal()):
            continue
        for point in line.get_points():
            add_point(vents, point[0], point[1])
    return vents


def add_point(vents, x, y):
    if y not in vents:
        vents[y] = {}
    if x not in vents[y]:
        vents[y][x] = 0
    vents[y][x] += 1


def count_intersections(vents):
    answer = 0
    for y in vents.keys():
        for x in vents[y].keys():
            if vents[y][x] > 1:
                answer += 1
    return answer


def add_diagonals(lines, vents):
    for line in lines:
        if not line.is_diagonal:
            continue
        for point in line.get_diagonal_points():
            add_point(vents, point[0], point[1])


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
