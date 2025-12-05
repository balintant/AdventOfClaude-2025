#!/usr/bin/env python3
"""
Day 5: Cafeteria - Part 2
https://adventofcode.com/2025/day/5

Count the total number of ingredient IDs considered fresh by the fresh ID ranges.
"""

import sys


def solve(data):
    """
    Count total ingredient IDs considered fresh by all ranges.

    Args:
        data: String containing the database with fresh ID ranges

    Returns:
        Total count of ingredient IDs covered by all fresh ranges
    """
    lines = data.strip().split("\n")

    # Find the blank line separating ranges from available IDs
    blank_line_idx = lines.index("")

    # Parse fresh ID ranges
    fresh_ranges = []
    for i in range(blank_line_idx):
        start, end = map(int, lines[i].split("-"))
        fresh_ranges.append((start, end))

    # Merge overlapping ranges to avoid double-counting
    # Sort ranges by start position
    fresh_ranges.sort()

    # Merge overlapping or adjacent ranges
    merged_ranges = []
    for start, end in fresh_ranges:
        if merged_ranges and start <= merged_ranges[-1][1] + 1:
            # Overlapping or adjacent - extend the last range
            merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], end))
        else:
            # Non-overlapping - add as new range
            merged_ranges.append((start, end))

    # Count total IDs in all merged ranges
    total_count = 0
    for start, end in merged_ranges:
        total_count += end - start + 1  # +1 because ranges are inclusive

    return total_count


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
