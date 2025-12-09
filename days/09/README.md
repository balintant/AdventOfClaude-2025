# Day 9: Movie Theater

## Problem Summary

The puzzle involves finding the largest rectangle on a tile floor with specific constraints:

**Part 1**: Find the largest rectangle where two red tiles serve as opposite corners. Any tiles can be inside the rectangle.

**Part 2**: Find the largest rectangle where:
- Two red tiles serve as opposite corners
- ALL tiles in the rectangle must be either red or green
- Green tiles form the edges connecting consecutive red tiles (which form a closed polygon) plus the interior of that polygon

## Solution Approach

### Part 1 - [part_1.py](part_1.py)

Simple brute force approach:
1. Parse all red tile coordinates
2. Try all pairs of red tiles as opposite corners
3. Calculate area for each rectangle: `(|x2 - x1| + 1) × (|y2 - y1| + 1)`
4. Return maximum area

**Time Complexity**: O(n²) where n is the number of red tiles
**Space Complexity**: O(n)

### Part 2 - [part_2.py](part_2.py)

The key insight is that coordinates are HUGE (up to ~98,000) but sparse (only 496 red tiles). The naive approach of checking every integer coordinate times out.

**Optimization Strategy**:
1. **Sparse coordinate processing**: Only compute polygon structure at y-coordinates that are vertices (496 coordinates instead of 50,000+)
2. **Scanline algorithm**: For each structural y-coordinate, compute x-intervals where the polygon exists
3. **Interval containment**: Check if rectangle is valid by testing if its x-extent is contained in polygon's x-intervals at each relevant y-coordinate
4. **Early termination**: Sort candidates by area descending and check corners first for quick rejection

**Algorithm**:
1. Build edge list from consecutive red tiles (forms closed polygon)
2. For each red tile's y-coordinate:
   - Use ray casting to find where vertical edges cross
   - Identify horizontal edges
   - Merge into x-intervals representing polygon extent at that y
3. For each candidate rectangle (sorted by area, largest first):
   - Check if all 4 corners are in/on polygon (quick rejection)
   - For each polygon y-coordinate in rectangle's y-range, verify x-extent [x_min, x_max] is contained in polygon's x-intervals
   - Return first valid rectangle (guaranteed to be largest)

**Key Optimization**: By only checking ~496 y-coordinates instead of ~50,000, the solution completes in under 30 seconds instead of timing out.

**Time Complexity**: O(n² log n) for sorting candidates + O(n² × k) for validation where k is average structural y-coordinates per rectangle
**Space Complexity**: O(n) for polygon structure

## Key Insights

1. **Sparse coordinates**: When coordinate ranges are huge but actual data points are sparse, work with the sparse set only
2. **Interval arithmetic**: Instead of point-by-point checking, use interval containment for entire ranges
3. **Scanline for rectilinear polygons**: For polygons with only horizontal/vertical edges, scanline algorithms efficiently compute interior regions
4. **Early termination**: Sorting by area and checking largest first allows immediate return on first valid rectangle

## Test Cases

### Part 1 Tests
- Example from puzzle (8 red tiles): Expected 50 ✓
- Two horizontal tiles: Expected 6 ✓
- Two vertical tiles: Expected 4 ✓
- Square corners: Expected 36 ✓

### Part 2 Tests
- Example from puzzle: Expected 24 ✓
- Simple 3×3 square: Expected 9 ✓

## Results

- **Part 1**: 4769758290
- **Part 2**: 1588990708

## Running the Solution

```bash
# Run Part 1
python3 part_1.py

# Run Part 2
python3 part_2.py

# Run tests
python3 test.py

# Using mise
mise run solve 9 1  # Part 1
mise run solve 9 2  # Part 2
mise run test 9     # All tests
```

## Performance Notes

The initial naive implementation for Part 2 timed out after 2+ minutes because it checked every integer coordinate in ranges of ~50,000-100,000. The optimized solution:
- Reduces y-coordinates checked from ~50,000 to ~496 (100x improvement)
- Uses O(1) interval containment instead of O(width) point-by-point checks
- Completes in well under 30 seconds
