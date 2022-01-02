# https://adventofcode.com/2021/day/17
import math
import sys
from ..common import *


def parse_area(area_str):
    start, end = area_str.split("=", 2)[1].split("..")
    return int(start), int(end)

def parse(data):
    x_area, y_area = data.split(": ", 2)[1].split(", ")
    x = parse_area(x_area)
    y = parse_area(y_area)
    return x, y


def launch(x_target, y_target, x_velocity, y_velocity):
    debug = False
    max_y = 0
    x, y = 0, 0
    while x < x_target[1] and y >= y_target[0]:
        if debug:
            print("-------------")
            print(f"x-vel:{x_velocity}, y-vel:{y_velocity}")
        x += x_velocity
        y += y_velocity
        if debug:
            print(f"x:{x}, y:{y}")
        if y > max_y:
            max_y = y
        if x_target[0] <= x <= x_target[1] and y_target[0] <= y <= y_target[1]:
            return True, max_y
        if x_velocity > 0:
            x_velocity -= 1
        elif x_velocity < 0:
            x_velocity += 1
        y_velocity -= 1
    return False, None

def part1(data):
    x, y = parse(data)
    candidates = []
    for i in range(x[1]):
        for j in range(math.floor(x[1]/2)):
            # print(i, j)
            hit, max_height = launch(x, y, i, j)
            if hit:
                candidates.append(max_height)
    return max(candidates)


def part2(data):
    return ""


data = "".join(read_data(sys.argv[1], str))
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")

