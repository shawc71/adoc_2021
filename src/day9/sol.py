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
            final.append(c)
    return final


def is_low_point(target_point, adjacent_pts, area):
    for point in adjacent_pts:
        if target_point >= area[point[0]][point[1]]:
            return False
    return True


def part1(data):
    area = parse(data)
    answer = 0
    for i, _ in enumerate(area):
        for j, _ in enumerate(area[i]):
            adjacent_pts = get_adjacent(i, j, area)
            if is_low_point(area[i][j], adjacent_pts, area):
                answer += area[i][j] + 1
    return answer


def calc_basin_size(curr_point, visited, area):
    i, j = curr_point
    if area[i][j] == 9:
        return 0

    adjacent_pts = list(filter(lambda pt: pt not in visited and area[pt[0]][pt[1]] != 9, get_adjacent(i, j, area)))
    # print(adjacent_pts)
    if not is_low_point(area[i][j], adjacent_pts, area):
        return 0

    visited.add((i, j))
    basin_size = 1
    for a in adjacent_pts:
        basin_size += calc_basin_size(a, visited, area)
    return basin_size


def solve_part2(data):
    area = parse(data)
    visited = set()
    basin_sizes = []
    for i, _ in enumerate(area):
        for j, _ in enumerate(area[i]):
            basin_size = calc_basin_size((i, j), visited, area)
            if basin_size > 0:
                basin_sizes.append(basin_size)
    # basin_sizes = sorted(basin_sizes)
    return basin_sizes


def part2(data):
    return solve_part2(data)


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
