def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row + 1
    j = col - 1
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve(board, col, n):
    if col == n:
        return True

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve(board, col + 1, n):
                return True

            board[row][col] = 0

    return False


n = int(input("Enter N: "))

board = [[0 for j in range(n)] for i in range(n)]

if solve(board, 0, n):
    print("Solution:")
    for row in board:
        print(row)
else:
    print("Solution does not exist")
