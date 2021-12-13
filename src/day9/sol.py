# https://adventofcode.com/2021/day/9
import sys
from ..common import read_data


def parse(lines):
    area = []
    for line in lines:
        row = list(map(lambda v: int(v), list(line)))
        area.append(row)
    return area


def get_adjacent(i, j, area):
    candidates = {
        (i - 1, j), (i + 1, j),
        (i, j - 1), (i, j + 1)
    }
    min_i = 0
    max_i = len(area)
    min_j = 0
    max_j = len(area[i])
    final = []
    for c in candidates:
        if min_i <= c[0] < max_i and min_j <= c[1] < max_j:
            final.append(area[c[0]][c[1]])
    return final


def is_low_point(target_point, adjacent_pts):
    for adj_point in adjacent_pts:
        if target_point >= adj_point:
            return False
    return True


def part1(data):
    area = parse(data)
    answer = 0
    for i, _ in enumerate(area):
        for j, _ in enumerate(area[i]):
            adjacent_pts = get_adjacent(i, j, area)
            if is_low_point(area[i][j], adjacent_pts):
                answer += area[i][j] + 1
    return answer


def part2(data):
    return ""


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
