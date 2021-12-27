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