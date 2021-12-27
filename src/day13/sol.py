# https://adventofcode.com/2021/day/13
import sys
from ..common import read_data, print_2d_array


def parse(lines):
    PARSING_DOTS = 0
    PARSING_FOLD_INSTRUCTIONS = 1
    state = PARSING_DOTS
    input = {
        'points': [],
        'transforms': [],
    }
    for line in lines:
        if line == "":
            state = PARSING_FOLD_INSTRUCTIONS
            continue
        if state == PARSING_DOTS:
            p = line.split(",")
            input['points'].append((int(p[0]), int(p[1])))
        else:
            transform = line.split(" ")[2].split("=")
            input['transforms'].append({
                'axis': transform[0],
                'magnitude': int(transform[1])
            })
    return input


def create_paper(rows, cols):
    paper = []
    for i in range(rows):
        paper.append([])
        for _ in range(cols):
            paper[i].append(".")
    return paper


def fill(paper, points):
    for p in points:
        paper[p[1]][p[0]] = "#"


def execute_transform(paper, transform, points):
    new_points = []
    if transform['axis'] == 'y':
        new_paper = create_paper(transform['magnitude'], len(paper[0]))
        for point in points:
            if point[1] < transform['magnitude']:
                new_points.append(point)
            else:
                y = (transform['magnitude'] * 2) - point[1]
                new_points.append((point[0], y))
    else:
        new_paper = create_paper(len(paper), transform['magnitude'])
        for point in points:
            if point[0] < transform['magnitude']:
                new_points.append(point)
            else:
                x = (transform['magnitude'] * 2) - point[0]
                new_points.append((x, point[1]))
    fill(new_paper, new_points)
    return new_paper, new_points


def count_visible(paper):
    count = 0
    for i, _ in enumerate(paper):
        for j, _ in enumerate(paper[i]):
            if paper[i][j] == "#":
                count += 1
    return count


def solve(data, only_first_transform):
    input = parse(data)
    rows = max(list(map(lambda p: p[1], input['points']))) + 1
    cols = max(list(map(lambda p: p[0], input['points']))) + 1
    paper = create_paper(rows, cols)
    fill(paper, input['points'])
    if only_first_transform:
        paper, _ = execute_transform(paper, input['transforms'][0], input['points'])
        return paper
    points = input['points']
    for transform in input['transforms']:
        paper, points = execute_transform(paper, transform, points)
    return paper


def part1(data):
    paper = solve(data, True)
    return count_visible(paper)


def part2(data):
    return solve(data, False)


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2:")
print_2d_array(part2(data), 1)
