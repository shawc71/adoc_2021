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


def part1(data):
    grid = parse(data)
    risks_from_origin = [[math.inf for _ in range(len(grid))] for _ in range(len(grid[0]))]
    risks_from_origin[0][0] = 0
    pq = []
    pq_lookup = {}
    for i, _ in enumerate(risks_from_origin):
        for j, _ in enumerate(risks_from_origin[i]):
            item = PqItem(risks_from_origin[i][j], (i, j))
            pq_lookup[item.data] = item
            heapq.heappush(pq, item)

    while len(pq) != 0:
        node = heapq.heappop(pq)
        for adj in get_adjacent_points(grid, node.data, False):
            candidate_risk = node.priority + grid[adj[0]][adj[1]]
            if candidate_risk < risks_from_origin[adj[0]][adj[1]]:
                risks_from_origin[adj[0]][adj[1]] = candidate_risk
                pq_lookup[adj].priority = candidate_risk
                heapq.heapify(pq)
    return risks_from_origin[len(risks_from_origin) - 1][len(risks_from_origin[0]) - 1]


def part2(data):
    return ""


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
