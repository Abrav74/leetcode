from typing import List


def isValidSudoku(self, board: List[List[str]]) -> bool:
    from collections import defaultdict

    rows = defaultdict(list)
    columns = defaultdict(list)
    squares = defaultdict(list)

    for row in range(1, 10):
        for col in range(1, 10):
            if board[row - 1][col - 1] == ".":
                continue
            rows[row].append(board[row - 1][col - 1])
            columns[col].append(board[row - 1][col - 1])

            box_row = (row - 1) // 3
            box_col = (col - 1) // 3

            if box_row == 0 and box_col == 0:
                squares[1].append(board[row - 1][col - 1])
            elif box_row == 1 and box_col == 0:
                squares[2].append(board[row - 1][col - 1])
            elif box_row == 2 and box_col == 0:
                squares[3].append(board[row - 1][col - 1])
            elif box_row == 0 and box_col == 1:
                squares[4].append(board[row - 1][col - 1])
            elif box_row == 1 and box_col == 1:
                squares[5].append(board[row - 1][col - 1])
            elif box_row == 2 and box_col == 1:
                squares[6].append(board[row - 1][col - 1])
            elif box_row == 0 and box_col == 2:
                squares[7].append(board[row - 1][col - 1])
            elif box_row == 1 and box_col == 2:
                squares[8].append(board[row - 1][col - 1])
            elif box_row == 2 and box_col == 2:
                squares[9].append(board[row - 1][col - 1])

    for row in rows:
        if len(rows[row]) is not len(set(rows[row])):
            print("row issue")
            return False
    for col in columns:
        if len(columns[col]) != len(set(columns[col])):
            print("col issue")
            return False
    for square in squares:
        if len(squares[square]) != len(set(squares[square])):
            print("square issue")
            return False
    return True
