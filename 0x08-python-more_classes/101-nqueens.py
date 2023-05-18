#!/usr/bin/python3

import sys


def print_solution(board):
    """Prints the board configuration as a solution to the N-queens problem"""
    for row in board:
        print(" ".join(row))


def is_safe(board, row, col, N):
    """Checks if it is safe to place a queen at the given position"""
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == "Q":
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    return True


def solve_nqueens(N):
    """Solves the N-queens problem and prints all possible solutions"""
    board = [["." for _ in range(N)] for _ in range(N)]
    solve_nqueens_helper(board, 0, N)


def solve_nqueens_helper(board, col, N):
    """Helper function to solve the N-queens problem using backtracking"""
    if col == N:
        print_solution(board)
        print()
        return

    for row in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = "Q"
            solve_nqueens_helper(board, col + 1, N)
            board[row][col] = "."


def main():
    """Main function"""
    # Check the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    main()
