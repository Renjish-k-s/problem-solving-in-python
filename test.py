def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    stack = []
    col = 0

    while True:
        placed = False
        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 'Q'
                stack.append((row, col))
                col += 1
                placed = True
                break

        if not placed:
            if not stack:
                break
            row, col = stack.pop()
            board[row][col] = '.'
            col -= 1

        if col == n:
            print_board(board)
            return True

    print("Solution does not exist")
    return False

# Example usage:
n = 8
solve_n_queens(n)
