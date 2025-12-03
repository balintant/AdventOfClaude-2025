#!/usr/bin/env python3
"""
Day 3: Lobby - Part 2
https://adventofcode.com/2025/day/3

Task: Find the maximum joltage from each battery bank by selecting exactly 12 batteries.
The joltage is the 12-digit number formed by the selected batteries (order preserved).

Strategy: Greedy approach - at each position, select the battery that gives the maximum
value for the remaining positions. This ensures we get the largest possible number.
"""

import sys


def find_max_joltage_12(bank: str) -> int:
    """
    Find the maximum 12-digit joltage from a battery bank.

    We need to pick exactly 12 batteries to form a 12-digit number.
    The order is preserved - we can only select batteries, not rearrange them.

    Strategy: Greedy algorithm - at each step, choose the position that
    maximizes the resulting number given the remaining positions to fill.

    Args:
        bank: String of digits representing battery joltage ratings

    Returns:
        Maximum 12-digit number that can be formed from 12 batteries
    """
    n = len(bank)
    if n < 12:
        # Not enough batteries
        return 0

    # We need to select 12 positions from n positions
    # Greedy approach: at each step, select the position with the maximum digit
    # that still leaves enough positions for the remaining selections

    selected_indices = []
    remaining_to_select = 12
    start_pos = 0

    for i in range(12):
        # How many positions do we need after this one?
        remaining_after = remaining_to_select - 1

        # We can select from positions [start_pos, n - remaining_after]
        # This ensures we have enough positions left for future selections
        max_digit = -1
        max_pos = start_pos

        for pos in range(start_pos, n - remaining_after):
            digit = int(bank[pos])
            if digit > max_digit:
                max_digit = digit
                max_pos = pos

        selected_indices.append(max_pos)
        start_pos = max_pos + 1
        remaining_to_select -= 1

    # Form the 12-digit number from selected positions
    result_str = "".join(bank[i] for i in selected_indices)
    return int(result_str)


def solve(banks: list[str]) -> int:
    """
    Find the total output joltage from all battery banks.

    Args:
        banks: List of battery bank strings (each is a line of digits)

    Returns:
        Sum of maximum 12-digit joltages from all banks
    """
    total = 0

    for bank in banks:
        max_joltage = find_max_joltage_12(bank)
        total += max_joltage

    return total


def solve_from_file(filename: str) -> int:
    """Solve using input from a file."""
    with open(filename, "r") as f:
        banks = [line.strip() for line in f if line.strip()]
    return solve(banks)


def main():
    """Main entry point - solve puzzle."""
    # Parse command line arguments
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    # Solve the actual puzzle
    answer = solve_from_file(input_file)
    print(answer)


if __name__ == "__main__":
    main()
