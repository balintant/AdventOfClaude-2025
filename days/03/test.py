#!/usr/bin/env python3
"""
Tests for Day 3: Lobby
"""

from part_1 import solve as solve_part1, find_max_joltage
from part_2 import solve as solve_part2, find_max_joltage_12


def test_find_max_joltage():
    """Test the find_max_joltage function with individual banks."""
    assert find_max_joltage("987654321111111") == 98, "987... should produce 98"
    assert find_max_joltage("811111111111119") == 89, "811...9 should produce 89"
    assert find_max_joltage("234234234234278") == 78, "...278 should produce 78"
    assert find_max_joltage("818181911112111") == 92, "...91... should produce 92"
    assert find_max_joltage("12") == 12, "12 should produce 12"
    assert find_max_joltage("99") == 99, "99 should produce 99"
    assert find_max_joltage("123") == 23, "123 should produce 23 (max of 12, 23)"
    print("✓ find_max_joltage tests passed")


def test_example_part1():
    """Test Part 1 with the example from the puzzle."""
    banks = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]

    # Expected: 98 + 89 + 78 + 92 = 357
    result = solve_part1(banks)
    expected = 357
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 1 example test passed: total = {result}")


def test_single_bank_part1():
    """Test with a single bank."""
    banks = ["987654321"]
    # Maximum is 98 from first two digits
    result = solve_part1(banks)
    expected = 98
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 1 single bank test passed: total = {result}")


def test_all_same_digits_part1():
    """Test with banks of all same digits."""
    banks = ["11111", "99999"]
    # 11111 -> 11, 99999 -> 99
    result = solve_part1(banks)
    expected = 11 + 99
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 1 all same digits test passed: total = {result}")


def test_ascending_descending_part1():
    """Test with ascending and descending sequences."""
    banks = ["123456789", "987654321"]
    # 123456789 -> 89 (last two)
    # 987654321 -> 98 (first two)
    result = solve_part1(banks)
    expected = 89 + 98
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 1 ascending/descending test passed: total = {result}")


def test_find_max_joltage_12():
    """Test the find_max_joltage_12 function with individual banks."""
    assert find_max_joltage_12("987654321111111") == 987654321111, (
        "Should select all except last 3 1s"
    )
    assert find_max_joltage_12("811111111111119") == 811111111119, (
        "Should select all except some 1s"
    )
    assert find_max_joltage_12("234234234234278") == 434234234278, (
        "Should skip some 2s and 3 at start"
    )
    assert find_max_joltage_12("818181911112111") == 888911112111, (
        "Should skip some 1s at start"
    )
    print("✓ find_max_joltage_12 tests passed")


def test_example_part2():
    """Test Part 2 with the example from the puzzle."""
    banks = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]

    # Expected: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619
    result = solve_part2(banks)
    expected = 3121910778619
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 2 example test passed: total = {result}")


def test_all_same_digits_part2():
    """Test Part 2 with banks of all same digits."""
    banks = ["111111111111", "999999999999"]
    # Both should just be the same 12 digits
    result = solve_part2(banks)
    expected = 111111111111 + 999999999999
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 2 all same digits test passed: total = {result}")


def test_descending_part2():
    """Test Part 2 with descending sequence."""
    banks = ["987654321987654"]
    # Greedy picks: 9(pos0), 8(pos1), 7(pos2), 6(pos3), 5(pos4), 4(pos5),
    # then 9(pos9), 8(pos10), 7(pos11), 6(pos12), 5(pos13), 4(pos14)
    # Result: 987654987654
    result = solve_part2(banks)
    expected = 987654987654
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ Part 2 descending test passed: total = {result}")


def run_tests():
    """Run all tests."""
    print("Running Day 3 tests...\n")
    print("=== Part 1 Tests ===")
    test_find_max_joltage()
    test_example_part1()
    test_single_bank_part1()
    test_all_same_digits_part1()
    test_ascending_descending_part1()
    print("\n=== Part 2 Tests ===")
    test_find_max_joltage_12()
    test_example_part2()
    test_all_same_digits_part2()
    test_descending_part2()
    print("\n✓ All tests passed!")


if __name__ == "__main__":
    run_tests()
