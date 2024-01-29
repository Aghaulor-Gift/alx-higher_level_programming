#!/usr/bin/python3
"""A module representing nqueen"""


import sys


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] +\
                i == col + row:
            return False
    return True


def print_solution(board, n):
    for i in range(n):
        row_str = ""
        for j in range(n):
            if j == board[i]:
                row_str += "Q"
            else:
                row_str += "."
        print(row_str)


def solve_nqueens_util(board, row, n):
    if row == n:
        print_solution(board, n)
        print()
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens_util(board, row + 1, n)


def solve_nqueens(n):
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens_util(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])
