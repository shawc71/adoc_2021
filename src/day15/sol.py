# https://adventofcode.com/2021/day/15
import math
import heapq
import sys
from ..common import *


class PqItem:
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data

    def __lt__(self, other):
        return self.priority < other.priority


def parse(data):
    grid = []
    for line in data:
        row = []
        for char in list(line):
            row.append(int(char))
        grid.append(row)
    return grid


def find_lowest_risk_path(grid):
    risks_from_origin = [[math.inf for _ in range(len(grid))] for _ in range(len(grid[0]))]
    risks_from_origin[0][0] = 0
    pq = []
    pq_lookup = {}
    item = PqItem(risks_from_origin[0][0], (0, 0))
    pq_lookup[item.data] = item
    heapq.heappush(pq, item)
    visited = set()
    while len(pq) != 0:
        node = heapq.heappop(pq)
        if node.data in visited:
            continue
        visited.add(node.data)
        for adj in get_adjacent_points(grid, node.data, False):
            if adj in visited:
                continue

            candidate_risk = node.priority + grid[adj[0]][adj[1]]
            if candidate_risk < risks_from_origin[adj[0]][adj[1]]:
                risks_from_origin[adj[0]][adj[1]] = candidate_risk
                if adj in pq_lookup:
                    pq_lookup[adj].priority = candidate_risk
                    heapq.heapify(pq)
                else:
                    item = PqItem(candidate_risk, adj)
                    pq_lookup[item.data] = item
                    heapq.heappush(pq, item)
    return risks_from_origin[len(risks_from_origin) - 1][len(risks_from_origin[0]) - 1]


def reformat_for_part2(grid):
    new_grid = [[0 for _ in range(len(grid) * 5)] for _ in range(len(grid[0]) * 5)]
    grid_len = len(grid)
    grid_width = len(grid[0])

    for i, _ in enumerate(new_grid):
        factor = math.floor(i / grid_len)
        for j, _ in enumerate(new_grid[i]):
            new_grid[i][j] = (grid[i % grid_len][j % grid_width] + factor)
            if new_grid[i][j] > 9:
                new_grid[i][j] = new_grid[i][j] % 9
            if (j + 1) % grid_width == 0:
                factor += 1
    return new_grid


def part1(data):
    return find_lowest_risk_path(parse(data))


def part2(data):
    grid = parse(data)
    return find_lowest_risk_path(reformat_for_part2(grid))


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
