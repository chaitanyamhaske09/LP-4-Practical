n = int(input("Enter value of N: "))

board = [[0] * n for i in range(n)]

# Place first queen
board[0][0] = 1

def safe(row, col):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row-1, col+1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve(row):

    if row == n:
        return True

    for col in range(n):
        if safe(row, col):
            board[row][col] = 1

            if solve(row + 1):
                return True

            # Backtracking
            board[row][col] = 0

    return False

if solve(0):
    print("N-Queens Solution:")
    for row in board:
        print(row)
else:
    print("No solution exists")
    
    
    
#     N-Queens Problem: It is a problem of placing N queens on an N×N chessboard so that no two queens attack each other.

# Backtracking: Backtracking is an algorithmic technique that tries possible solutions and goes back whenever a choice leads to an invalid solution.

# Working:
# 1. Create an N×N matrix filled with zeros.
# 2. Place the first queen at position (0,0).
# 3. Check whether the next queen can be placed safely.
# 4. Place the queen if the position is safe.
# 5. If no safe position exists, go back and change the previous queen's position.
# 6. Repeat until all queens are placed.
# 5. Time and Space Complexity
# Complexity	Value
# Time Complexity	O(N!) (upper-bound commonly used)
# Space Complexity	O(N²)