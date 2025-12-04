#!/usr/bin/env python3
"""
Day 4: Printing Department - Part 2
https://adventofcode.com/2025/day/4

Task: Iteratively remove accessible paper rolls until no more can be removed.
A roll can be accessed if it has fewer than 4 adjacent rolls (8-directional neighbors).
After removing accessible rolls, more rolls may become accessible.

Grid notation:
- '@' = paper roll
- '.' = empty space
"""

import sys


def count_adjacent_rolls(grid: list[list[str]], r: int, c: int) -> int:
    """
    Count adjacent paper rolls for a given position.

    Args:
        grid: 2D grid (mutable)
        r: Row index
        c: Column index

    Returns:
        Number of adjacent paper rolls (0-8)
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # 8 directions: N, NE, E, SE, S, SW, W, NW
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    adjacent_count = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == "@":
                adjacent_count += 1

    return adjacent_count


def find_accessible_rolls(grid: list[list[str]]) -> list[tuple[int, int]]:
    """
    Find all accessible paper rolls in the current grid state.

    Args:
        grid: 2D grid (mutable)

    Returns:
        List of (row, col) tuples for accessible rolls
    """
    accessible = []
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                if count_adjacent_rolls(grid, r, c) < 4:
                    accessible.append((r, c))

    return accessible


def remove_rolls_iteratively(grid: list[str]) -> int:
    """
    Iteratively remove accessible rolls until no more can be removed.

    Args:
        grid: List of strings representing the initial grid

    Returns:
        Total number of rolls removed
    """
    if not grid:
        return 0

    # Convert to mutable 2D list
    mutable_grid = [list(row) for row in grid]
    total_removed = 0

    while True:
        # Find all accessible rolls in current state
        accessible = find_accessible_rolls(mutable_grid)

        if not accessible:
            # No more rolls can be removed
            break

        # Remove all accessible rolls
        for r, c in accessible:
            mutable_grid[r][c] = "."

        total_removed += len(accessible)

    return total_removed


def solve(grid: list[str]) -> int:
    """
    Solve the puzzle.

    Args:
        grid: List of strings representing the grid

    Returns:
        Total number of rolls that can be removed
    """
    return remove_rolls_iteratively(grid)


def solve_from_file(filename: str) -> int:
    """Solve using input from a file."""
    with open(filename, "r") as f:
        grid = [line.rstrip("\n") for line in f]
    return solve(grid)


def main():
    """Main entry point - solve puzzle."""
    # Parse command line arguments
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    # Solve the actual puzzle
    answer = solve_from_file(input_file)
    print(answer)


if __name__ == "__main__":
    main()
