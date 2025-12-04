#!/usr/bin/env python3
"""
Tests for Day 4: Printing Department
"""

from part_1 import solve as solve_part1


def test_example_part1():
    """Test Part 1 with the example from the puzzle."""
    grid = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]

    # Expected: 13 accessible rolls
    result = solve_part1(grid)
    expected = 13
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 1 example test passed: accessible rolls = {result}")


def test_single_roll_part1():
    """Test with a single isolated roll."""
    grid = [
        "...",
        ".@.",
        "...",
    ]
    # Single roll with 0 adjacent rolls -> accessible
    result = solve_part1(grid)
    expected = 1
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 1 single roll test passed: accessible rolls = {result}")


def test_surrounded_roll_part1():
    """Test with a roll surrounded by 8 rolls."""
    grid = [
        "@@@",
        "@@@",
        "@@@",
    ]
    # Center roll has 8 adjacent rolls -> not accessible
    # Corner and edge rolls have 3-5 adjacent rolls -> some accessible
    result = solve_part1(grid)
    # Corners: 3 adjacent each (4 corners) -> 4 accessible
    # Edges: 5 adjacent each (4 edges) -> 0 accessible
    # Center: 8 adjacent -> 0 accessible
    expected = 4
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 1 surrounded roll test passed: accessible rolls = {result}")


def test_line_of_rolls_part1():
    """Test with a horizontal line of rolls."""
    grid = [
        ".....",
        "@@@@@",
        ".....",
    ]
    # Each roll has at most 2 adjacent rolls -> all accessible
    result = solve_part1(grid)
    expected = 5
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 1 line of rolls test passed: accessible rolls = {result}")


def test_no_rolls_part1():
    """Test with no paper rolls."""
    grid = [
        "....",
        "....",
        "....",
    ]
    result = solve_part1(grid)
    expected = 0
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 1 no rolls test passed: accessible rolls = {result}")


def run_tests():
    """Run all tests."""
    print("Running Day 4 tests...\n")
    print("=== Part 1 Tests ===")
    test_example_part1()
    test_single_roll_part1()
    test_surrounded_roll_part1()
    test_line_of_rolls_part1()
    test_no_rolls_part1()
    print("\n✓ All tests passed!")


if __name__ == "__main__":
    run_tests()
