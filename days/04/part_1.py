#!/usr/bin/env python3
"""
Day 4: Printing Department - Part 1
https://adventofcode.com/2025/day/4

Task: Count rolls of paper that can be accessed by a forklift.
A roll can be accessed if it has fewer than 4 adjacent rolls (8-directional neighbors).

Grid notation:
- '@' = paper roll
- '.' = empty space
"""

import sys


def count_accessible_rolls(grid: list[str]) -> int:
    """
    Count paper rolls that can be accessed by a forklift.

    A roll at position (r, c) can be accessed if it has fewer than 4
    adjacent rolls in the 8 surrounding positions.

    Args:
        grid: List of strings representing the grid

    Returns:
        Number of accessible paper rolls
    """
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    accessible_count = 0

    # 8 directions: N, NE, E, SE, S, SW, W, NW
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    for r in range(rows):
        for c in range(cols):
            # Only check paper rolls
            if grid[r][c] != "@":
                continue

            # Count adjacent paper rolls
            adjacent_rolls = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check bounds
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == "@":
                        adjacent_rolls += 1

            # Accessible if fewer than 4 adjacent rolls
            if adjacent_rolls < 4:
                accessible_count += 1

    return accessible_count


def solve(grid: list[str]) -> int:
    """
    Solve the puzzle.

    Args:
        grid: List of strings representing the grid

    Returns:
        Number of accessible paper rolls
    """
    return count_accessible_rolls(grid)


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
