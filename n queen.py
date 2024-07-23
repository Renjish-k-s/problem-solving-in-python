N = 8
board = [[0] * N for _ in range(N)]

def isattack(i, j):
    for k in range(N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    for k in range(N):
        for l in range(N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True

    return False

def nqueens(n):
    if n == 0:
        for row in board:
            print(row)
        return True

    for i in range(N):
        for j in range(N):
            if not isattack(i, j) and board[i][j] != 1:
                board[i][j] = 1
                if nqueens(n - 1):
                    return True
                board[i][j] = 0  

    return False

# Example usage:
nqueens(N)
