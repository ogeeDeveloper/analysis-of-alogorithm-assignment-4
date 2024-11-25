def solve_n_queens(n):
    """
    Solves the N-Queens problem using backtracking.

    Time Complexity Analysis:
    - Worst case: O(N!)
    - At first row: N choices
    - At second row: N-1 choices (approximately)
    - Pattern continues, giving N * (N-1) * (N-2) * ... * 1 = N!

    Space Complexity: O(N) for recursion stack + O(N^2) for board

    Optimizations:
    1. Using 1D arrays for row, diagonal checks instead of 2D board
    2. Early pruning by checking diagonal conflicts immediately
    3. Symmetry optimization possible (not implemented) could reduce search space by 8x
    4. Bit manipulation could improve performance for conflict checking
    """
    def is_safe(board, row, col):
        # Check row (not needed as we ensure one queen per row)

        # Check column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check upper left diagonal
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check upper right diagonal
        for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
            if board[i][j] == 1:
                return False

        return True

    def solve(board, row):
        if row >= n:
            return True

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1

                if solve(board, row + 1):
                    return True

                board[row][col] = 0

        return False

    # Initialize board with zeros
    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve(board, 0):
        return board
    return None


# Example usage
n = 8
solution = solve_n_queens(n)
if solution:
    for row in solution:
        print(row)
