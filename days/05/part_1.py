#!/usr/bin/env python3
"""
Day 5: Cafeteria - Part 1
https://adventofcode.com/2025/day/5

Determine how many available ingredient IDs are fresh based on the fresh ID ranges.
"""

import sys


def solve(data):
    """
    Solve the cafeteria ingredient freshness puzzle.

    Args:
        data: String containing the database with fresh ID ranges and available IDs

    Returns:
        Number of available ingredient IDs that are fresh
    """
    lines = data.strip().split("\n")

    # Find the blank line separating ranges from available IDs
    blank_line_idx = lines.index("")

    # Parse fresh ID ranges
    fresh_ranges = []
    for i in range(blank_line_idx):
        start, end = map(int, lines[i].split("-"))
        fresh_ranges.append((start, end))

    # Parse available ingredient IDs
    available_ids = []
    for i in range(blank_line_idx + 1, len(lines)):
        available_ids.append(int(lines[i]))

    # Count how many available IDs are fresh
    fresh_count = 0
    for ingredient_id in available_ids:
        # Check if ID falls within any fresh range (inclusive)
        for start, end in fresh_ranges:
            if start <= ingredient_id <= end:
                fresh_count += 1
                break  # No need to check other ranges once we find a match

    return fresh_count


def solve_from_file(filename):
    """Read input from file and solve the puzzle."""
    with open(filename, "r") as f:
        data = f.read()
    return solve(data)


def main():
    """Main entry point for the solution."""
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    result = solve_from_file(filename)
    print(result)


if __name__ == "__main__":
    main()
