def read_data(data_file, evaluator=str):
    with open(data_file) as f:
        return [evaluator(v) for v in f.read().rstrip().split("\n")]