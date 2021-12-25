# https://adventofcode.com/2021/day/11
import sys
from ..common import read_data

SHOULD_LIGHT_UP = 10
lit_up_count = 0


def parse(data):
    grid = []
    for line in data:
        grid.append(list(map(lambda x: int(x), list(line))))
    return grid


def increment_energy(grid):
    for i, _ in enumerate(grid):
        for j, _ in enumerate(grid[i]):
            grid[i][j] += 1


def get_adjacent_points(grid, point):
    i = point[0]
    j = point[1]
    candidates = [
        (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
        (i, j - 1), (i, j + 1),
        (i + 1, j - 1), (i + 1, j), (i + 1, j + 1),
    ]
    final = []
    for c in candidates:
        if 0 <= c[0] < len(grid) and 0 <= c[1] < len(grid[c[0]]):
            final.append(c)
    return final


def light_up_point(grid, point, already_lit_up):
    global lit_up_count
    if point in already_lit_up:
        return
    grid[point[0]][point[1]] = 0
    lit_up_count += 1
    already_lit_up.add(point)
    for adj in get_adjacent_points(grid, point):
        if adj in already_lit_up or grid[adj[0]][adj[1]] == SHOULD_LIGHT_UP:
            continue
        grid[adj[0]][adj[1]] += 1
    for adj in get_adjacent_points(grid, point):
        if adj in already_lit_up:
            continue
        if grid[adj[0]][adj[1]] == SHOULD_LIGHT_UP:
            light_up_point(grid, adj, already_lit_up)


def light_up(grid, already_lit_up):
    for i, _ in enumerate(grid):
        for j, _ in enumerate(grid[i]):
            if grid[i][j] == SHOULD_LIGHT_UP:
                light_up_point(grid, (i, j), already_lit_up)

def print_grid(grid):
    for i, _ in enumerate(grid):
        for j, _ in enumerate(grid[i]):
            formatted_num = grid[i][j]
            if formatted_num < 10:
                formatted_num = f" {formatted_num}"
            print(f"{formatted_num} ", end='')
        print()

def part1(data):
    global lit_up_count
    grid = parse(data)
    total_steps = 100
    for i in range(total_steps):
        already_lit_up = set()
        increment_energy(grid)
        light_up(grid, already_lit_up)

    return lit_up_count


def part2(data):
    step = 0
    grid = parse(data)
    while True:
        already_lit_up = set()
        increment_energy(grid)
        light_up(grid, already_lit_up)
        step += 1
        all_lit = True
        for i, _ in enumerate(grid):
            for j, _ in enumerate(grid[i]):
                if grid[i][j] != 0:
                    all_lit = False
        if all_lit:
            return step


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
