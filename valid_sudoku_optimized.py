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
            if board[row - 1][col - 1] in rows[row]:
                return False
            if board[row - 1][col - 1] in columns[col]:
                return False
            rows[row].append(board[row - 1][col - 1])
            columns[col].append(board[row - 1][col - 1])

            box_row = (row - 1) // 3
            box_col = (col - 1) // 3

            square = str(box_row) + str(box_col)

            if board[row - 1][col - 1] in squares[square]:
                return False
            squares[square].append(board[row - 1][col - 1])

    return True
