# Day 5: Cafeteria

## Problem Summary

The Elves have a new inventory management system that tracks ingredient freshness using ID ranges. The puzzle provides:
1. A list of fresh ingredient ID ranges (inclusive, can overlap)
2. A list of available ingredient IDs

**Part 1:** Count how many of the available ingredient IDs are fresh (i.e., fall within at least one fresh ID range).

**Part 2:** Count the total number of unique ingredient IDs that are considered fresh by all the fresh ID ranges (ignoring the available IDs list).

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

### Part 2 - [part_2.py](part_2.py)

Part 2 requires counting all unique ingredient IDs covered by the fresh ranges, not just checking specific available IDs. The key challenge is handling overlapping ranges efficiently:

1. **Parse the input** to extract only the fresh ID ranges (ignore the available IDs section)

2. **Sort ranges** by start position to prepare for merging

3. **Merge overlapping and adjacent ranges**:
   - Iterate through sorted ranges
   - If a range overlaps or is adjacent to the previous range (`start <= prev_end + 1`), extend the previous range
   - Otherwise, start a new merged range
   - This eliminates double-counting of IDs

4. **Count total IDs** in all merged ranges:
   - For each merged range: `count = end - start + 1` (inclusive)
   - Sum all counts

**Time Complexity:** O(m log m) where m is the number of ranges (dominated by sorting)
**Space Complexity:** O(m) for storing merged ranges

**Why merging is necessary:** Without merging, overlapping ranges like `10-14` and `12-18` would count IDs 12, 13, and 14 twice.

## Key Insights

- Ranges are **inclusive**: `3-5` includes IDs 3, 4, and 5
- Ranges can **overlap**: an ID is fresh if it's in *any* range
- Single-value ranges are possible (e.g., `390522922084641-390522922084641`)
- **Part 1 optimization:** Early termination - once an ID matches any range, no need to check remaining ranges
- **Part 2 optimization:** Merge overlapping/adjacent ranges to avoid double-counting and reduce computation
- Adjacent ranges (e.g., `1-5` and `6-10`) should be merged since they represent a continuous set of IDs

## Test Cases

The [test.py](test.py) file includes:

**Part 1 Tests:**
1. **Example test** - The puzzle's example with 3 fresh IDs out of 6 available
2. **Single range test** - Verify basic range checking works
3. **Overlapping ranges test** - Ensure overlaps are handled correctly
4. **No fresh test** - Edge case where no IDs are fresh
5. **All fresh test** - Edge case where all IDs are fresh

**Part 2 Tests:**
1. **Example test** - The puzzle's example expecting 14 total unique IDs
2. **Single range test** - Verify counting IDs in a single range
3. **Overlapping ranges test** - Verify ranges are merged correctly (5-10 + 7-12 = 8 IDs)
4. **Non-overlapping ranges test** - Verify separate ranges are counted independently
5. **Adjacent ranges test** - Verify adjacent ranges are merged (1-5 + 6-10 = 10 IDs)
6. **Single-ID ranges test** - Verify ranges with same start and end work correctly

## Results

- **Part 1:** 613
- **Part 2:** 336495597913098

## Running Instructions

Using mise tasks:
```bash
mise run solve 5 1    # Run Part 1
mise run solve 5 2    # Run Part 2
mise run solve 5      # Run both parts
mise run test 5       # Run all tests
```

Direct Python execution:
```bash
cd days/05
python3 part_1.py              # Run Part 1 with input.txt
python3 part_2.py              # Run Part 2 with input.txt
python3 part_1.py custom.txt   # Run with custom input
python3 test.py                # Run all tests
```
