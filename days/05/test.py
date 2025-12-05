#!/usr/bin/env python3
"""
Test suite for Day 5: Cafeteria
"""

from part_1 import solve as solve_part1
from part_2 import solve as solve_part2


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


def test_example_part2():
    """Test the example from Part 2 puzzle description."""
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
    result = solve_part2(data)
    # Ranges: 3-5 (3 IDs), 10-14 (5 IDs), 12-18 merged with 16-20 -> 12-20 (9 IDs)
    # Total: 3 + 5 + 9 = 17... wait, let me recalculate
    # 3-5: 3,4,5 (3 IDs)
    # 10-14: 10,11,12,13,14 (5 IDs)
    # 16-20: 16,17,18,19,20 (5 IDs)
    # 12-18: 12,13,14,15,16,17,18 (7 IDs)
    # Unique: 3,4,5,10,11,12,13,14,15,16,17,18,19,20 = 14 IDs
    expected = 14
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ test_example_part2 passed")


def test_single_range_part2():
    """Test with a single range."""
    data = """1-10

5
15
20"""
    result = solve_part2(data)
    expected = 10  # IDs 1-10 inclusive
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ test_single_range_part2 passed")


def test_overlapping_ranges_part2():
    """Test with overlapping ranges that should be merged."""
    data = """5-10
7-12

6
8
13"""
    result = solve_part2(data)
    # Ranges 5-10 and 7-12 overlap, so merge to 5-12 = 8 IDs
    expected = 8  # IDs 5,6,7,8,9,10,11,12
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ test_overlapping_ranges_part2 passed")


def test_non_overlapping_ranges_part2():
    """Test with non-overlapping ranges."""
    data = """1-5
10-15

7
8
20"""
    result = solve_part2(data)
    # 1-5 = 5 IDs, 10-15 = 6 IDs, total = 11 IDs
    expected = 11
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ test_non_overlapping_ranges_part2 passed")


def test_adjacent_ranges_part2():
    """Test with adjacent ranges that should be merged."""
    data = """1-5
6-10

3
7
15"""
    result = solve_part2(data)
    # 1-5 and 6-10 are adjacent, merge to 1-10 = 10 IDs
    expected = 10
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ test_adjacent_ranges_part2 passed")


def test_single_id_range_part2():
    """Test with single-ID ranges."""
    data = """5-5
10-10
15-15

5
10
20"""
    result = solve_part2(data)
    # Three single IDs: 5, 10, 15 = 3 IDs
    expected = 3
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ test_single_id_range_part2 passed")


def run_tests():
    """Run all test functions."""
    print("\n=== Part 1 Tests ===")
    test_example_part1()
    test_single_range_part1()
    test_overlapping_ranges_part1()
    test_no_fresh_part1()
    test_all_fresh_part1()

    print("\n=== Part 2 Tests ===")
    test_example_part2()
    test_single_range_part2()
    test_overlapping_ranges_part2()
    test_non_overlapping_ranges_part2()
    test_adjacent_ranges_part2()
    test_single_id_range_part2()

    print("\n✓ All tests passed!\n")


if __name__ == "__main__":
    run_tests()
