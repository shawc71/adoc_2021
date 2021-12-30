def read_data(data_file, evaluator=str):
    with open(data_file) as f:
        return [evaluator(v) for v in f.read().rstrip().split("\n")]


def print_2d_array(grid, chars_per_slot):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pad = chars_per_slot - len(str(grid[i][j]))
            formatted = f"{' ' * pad}{grid[i][j]}"
            print(formatted, end="")
        print("")


def get_adjacent_points(grid, point, include_diagonals):
    i = point[0]
    j = point[1]
    candidates = []
    if not include_diagonals:
        candidates.extend([
            (i - 1, j), (i + 1, j),
            (i, j - 1), (i, j + 1)
        ])
    else:
        candidates.extend([
            (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
            (i, j - 1), (i, j + 1),
            (i + 1, j - 1), (i + 1, j), (i + 1, j + 1),
        ])
    final = []
    for c in candidates:
        if 0 <= c[0] < len(grid) and 0 <= c[1] < len(grid[c[0]]):
            final.append(c)
    return final
