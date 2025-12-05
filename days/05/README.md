# Day 5: Cafeteria

## Problem Summary

The Elves have a new inventory management system that tracks ingredient freshness using ID ranges. The puzzle provides:
1. A list of fresh ingredient ID ranges (inclusive, can overlap)
2. A list of available ingredient IDs

**Part 1:** Count how many of the available ingredient IDs are fresh (i.e., fall within at least one fresh ID range).

## Solution Approach

### Part 1 - [part_1.py](part_1.py)

The solution uses a straightforward range-checking algorithm:

1. **Parse the input** by splitting on the blank line:
   - Lines before the blank line are fresh ID ranges (format: `start-end`)
   - Lines after the blank line are available ingredient IDs

2. **For each available ID**, check if it falls within any fresh range:
   - Iterate through all fresh ranges
   - Check if `start <= ingredient_id <= end` (inclusive bounds)
   - If a match is found, count it as fresh and break (no need to check remaining ranges)

3. **Return the count** of fresh ingredient IDs

**Time Complexity:** O(n × m) where n is the number of available IDs and m is the number of ranges
**Space Complexity:** O(n + m) for storing the parsed ranges and IDs

## Key Insights

- Ranges are **inclusive**: `3-5` includes IDs 3, 4, and 5
- Ranges can **overlap**: an ID is fresh if it's in *any* range
- Single-value ranges are possible (e.g., `390522922084641-390522922084641`)
- Early termination optimization: once an ID matches any range, no need to check remaining ranges

## Test Cases

The [test.py](test.py) file includes:

1. **Example test** - The puzzle's example with 3 fresh IDs out of 6 available
2. **Single range test** - Verify basic range checking works
3. **Overlapping ranges test** - Ensure overlaps are handled correctly
4. **No fresh test** - Edge case where no IDs are fresh
5. **All fresh test** - Edge case where all IDs are fresh

All tests verify the correct count of fresh ingredient IDs.

## Results

- **Part 1:** 613

## Running Instructions

Using mise tasks:
```bash
mise run solve 5 1    # Run Part 1
mise run test 5       # Run all tests
```

Direct Python execution:
```bash
cd days/05
python3 part_1.py              # Run Part 1 with input.txt
python3 part_1.py custom.txt   # Run with custom input
python3 test.py                # Run all tests
```
