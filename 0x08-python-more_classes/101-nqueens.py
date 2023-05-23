#!/usr/bin/python3

import sys

def is_safe(board, row, col):
    # Check if a queen can be placed at the given position without attacking any other queen

    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check if there is a queen in the upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(board, row, solutions):
    # Recursive function to solve the N queens problem using backtracking

    # Base case: if all queens are placed, add the solution to the list of solutions
    if row == len(board):
        solutions.append([''.join(row) for row in board])
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            # Place the queen at the current position
            board[row][col] = 'Q'

            # Recursively solve the problem for the next row
            solve_nqueens(board, row + 1, solutions)

            # Remove the queen from the current position for backtracking
            board[row][col] = '.'

def print_solutions(n):
    # Print all the solutions to the N queens problem

    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    solve_nqueens(board, 0, solutions)

    for solution in solutions:
        for row in solution:
            print(row)
        print()

def main():
    # Check the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    print_solutions(n)

if __name__ == '__main__':
    main()
