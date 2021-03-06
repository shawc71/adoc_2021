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


def paths_to_end_2(start_cave, graph, visited_small_caves, can_visit_twice, path, valid_paths):
    global accum
    to_end = 0
    for next_cave in graph[start_cave]:
        if next_cave == 'start':
            continue
        if (next_cave == can_visit_twice and can_visit_twice in visited_small_caves and visited_small_caves[
            can_visit_twice] > 1) or \
                (next_cave != can_visit_twice and (
                        next_cave in visited_small_caves and visited_small_caves[next_cave] == 1)):
            continue
        if next_cave == 'end':
            valid_paths.add("".join(path))
            to_end += 1
        else:
            if is_small(next_cave):
                if next_cave not in visited_small_caves:
                    visited_small_caves[next_cave] = 0
                visited_small_caves[next_cave] += 1
            path.append(next_cave)
            to_end += paths_to_end_2(next_cave, graph, visited_small_caves, can_visit_twice, path, valid_paths)
            path.pop()
            if is_small(next_cave):
                if visited_small_caves[next_cave] == 0:
                    visited_small_caves[next_cave] = 0
                else:
                    visited_small_caves[next_cave] -= 1
    return to_end


def part2(data):
    graph = parse(data)
    path_count = 0
    small_caves = []
    for key in graph:
        if is_small(key) and key != 'start' and key != 'end':
            small_caves.append(key)
    valid_paths = set()
    for cave in graph['start']:
        for can_visit_twice in small_caves:
            visited_small_caves = {}
            path = [cave]
            if is_small(cave):
                visited_small_caves[cave] = 1
            path_count += paths_to_end_2(cave, graph, visited_small_caves, can_visit_twice, path, valid_paths)
    return len(valid_paths)


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
