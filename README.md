# Algorithm Analysis Solutions for Assignment 4

Implementation of backtracking algorithms for solving combinatorial problems.

## Problems Solved

1. N-Queens Problem
2. Subset Sum Problem
3. Sudoku Solver

## 1. N-Queens Problem

Places N queens on an NxN chessboard without conflicts.

### Time Complexity

- O(N!) worst case
- Space: O(N) for recursion + O(N²) for board

### Features

- Solution validation
- Position conflict checking
- Optimization techniques
- Board visualization

## 2. Subset Sum Problem

Finds subset of integers summing to target value.

### Time Complexity

- O(2^N) worst case
- Space: O(N) recursion depth

### Features

- Early termination
- Sorted input optimization
- Multiple solutions handling
- Performance analysis

## 3. Sudoku Solver

Solves 9x9 Sudoku puzzles using backtracking.

### Time Complexity

- O(9^(N²)) worst case
- Space: O(N²) recursion depth

### Features

- Multiple difficulty levels
- Performance metrics
- Rule validation
- Solution visualization