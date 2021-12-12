# https://adventofcode.com/2021/day/4
import sys
from ..common import read_data


class Board:
    def __init__(self, id):
        self.id = id
        self.rows = []
        self.slot_lookup = {}

    def add_row(self, row):
        slots = []
        for i, num in enumerate(row):
            assert num not in self.slot_lookup
            slot = {
                'num': num,
                'marked': False,
                'col_idx': i,
                'row_idx': len(self.rows)
            }
            slots.append(slot)
            self.slot_lookup[slot['num']] = slot
        self.rows.append(slots)

    def mark(self, number):
        if number not in self.slot_lookup:
            return False
        self.slot_lookup[number]['marked'] = True
        return self.is_bingo(self.slot_lookup[number])

    def is_bingo(self, slot):
        return self.is_row_marked(slot['row_idx']) or self.is_col_marked(slot['col_idx'])

    def is_row_marked(self, row_idx):
        for j, _ in enumerate(self.rows[row_idx]):
            if not self.rows[row_idx][j]['marked']:
                return False
        return True

    def is_col_marked(self, col_idx):
        for i, _ in enumerate(self.rows):
            if not self.rows[i][col_idx]['marked']:
                return False
        return True

    def unmarked_sum(self):
        running_sum = 0
        for row in self.rows:
            for slot in row:
                if not slot['marked']:
                    running_sum += slot['num']
        return running_sum

    def print(self):
        for row in self.rows:
            for slot in row:
                marked = '.'
                if slot['marked']:
                    marked = 'x'
                formatted_num = slot['num']
                if formatted_num < 10:
                    formatted_num = f" {formatted_num}"
                print(f"{formatted_num}({marked}) ", end='')
            print("")


def parse_input(data):
    draws = []
    boards = []
    curr_board = None
    board_id = 0
    for i, line in enumerate(data):
        line = line.strip()
        if i == 0:
            draws = list(map(lambda val: int(val), data[i].split(",")))
        elif line == "":
            if curr_board is not None:
                boards.append(curr_board)
            curr_board = Board(board_id)
            board_id += 1
        else:
            row = list(map(lambda val: int(val.strip()), line.split()))
            curr_board.add_row(row)
    boards.append(curr_board)
    return {
        'draws': draws,
        'boards': boards,
    }


def part1(data):
    bingo = parse_input(data)
    for draw in bingo['draws']:
        for board in bingo['boards']:
            is_bingo = board.mark(draw)
            if is_bingo:
                return draw * board.unmarked_sum()
    return None


def part2(data):
    bingo = parse_input(data)
    winners = set()
    last_winner = None
    for draw in bingo['draws']:
        for board in bingo['boards']:
            if board.id in winners:
                continue
            is_bingo = board.mark(draw)
            if is_bingo:
                winners.add(board.id)
                last_winner = draw * board.unmarked_sum()
    return last_winner


data = read_data(sys.argv[1], str)
print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
