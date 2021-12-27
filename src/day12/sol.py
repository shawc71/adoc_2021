# https://adventofcode.com/2021/day/12
import sys
from ..common import read_data


def is_start(cave):
    return cave == "start"


def is_end(cave):
    return cave == "end"


def is_small(cave):
    return cave.islower()


def parse(lines):
    graph = {}
    for line in lines:
        path = line.split("-", 2)
        if path[0] not in graph:
            graph[path[0]] = set()
        graph[path[0]].add(path[1])
        if path[1] not in graph:
            graph[path[1]] = set()
        graph[path[1]].add(path[0])
    return graph

def paths_to_end(start_cave, graph, visited_small_caves):
    to_end = 0
    for next_cave in graph[start_cave]:
        if next_cave == 'start':
            continue
        if next_cave in visited_small_caves:
            continue
        if next_cave == 'end':
            to_end += 1
        else:
            if is_small(next_cave):
                visited_small_caves.add(next_cave)
            to_end += paths_to_end(next_cave, graph, visited_small_caves)
            if is_small(next_cave):
                visited_small_caves.remove(next_cave)
    return to_end

def part1(data):
    graph = parse(data)
    path_count = 0
    for cave in graph['start']:
        visited_small_caves = set()
        if is_small(cave):
            visited_small_caves.add(cave)
        path_count += paths_to_end(cave, graph, visited_small_caves)
    return path_count


def part2(data):
    return ""


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
