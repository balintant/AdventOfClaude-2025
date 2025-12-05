#!/usr/bin/env python3
"""
Test suite for Day 5: Cafeteria
"""

from part_1 import solve as solve_part1
# from part_2 import solve as solve_part2  # Uncomment when Part 2 is ready


def test_example_part1():
    """Test the example from the puzzle description."""
    data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    result = solve_part1(data)
    expected = 3  # IDs 5, 11, and 17 are fresh
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ test_example_part1 passed")


def test_single_range_part1():
    """Test with a single range."""
    data = """1-10

5
15
20"""
    result = solve_part1(data)
    expected = 1  # Only ID 5 is fresh
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ test_single_range_part1 passed")


def test_overlapping_ranges_part1():
    """Test with completely overlapping ranges."""
    data = """5-10
7-12

6
8
13"""
    result = solve_part1(data)
    expected = 2  # IDs 6 and 8 are fresh, 13 is spoiled
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ test_overlapping_ranges_part1 passed")


def test_no_fresh_part1():
    """Test when no available IDs are fresh."""
    data = """1-5
10-15

7
8
20"""
    result = solve_part1(data)
    expected = 0  # None are fresh
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ test_no_fresh_part1 passed")


def test_all_fresh_part1():
    """Test when all available IDs are fresh."""
    data = """1-100

5
25
50
75"""
    result = solve_part1(data)
    expected = 4  # All are fresh
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ test_all_fresh_part1 passed")


def run_tests():
    """Run all test functions."""
    print("\n=== Part 1 Tests ===")
    test_example_part1()
    test_single_range_part1()
    test_overlapping_ranges_part1()
    test_no_fresh_part1()
    test_all_fresh_part1()
    print("\n✓ All tests passed!\n")


if __name__ == "__main__":
    run_tests()
