# Day 4: Printing Department

## Problem Summary

The puzzle involves optimizing forklift work by identifying which paper rolls can be accessed.

- **Part 1**: Count paper rolls that have fewer than 4 adjacent rolls (8-directional neighbors)

## Solution Approach

### Part 1 ([part_1.py](part_1.py))

The solution checks each paper roll and counts its adjacent neighbors:

1. **Grid Traversal**: Iterate through each cell in the grid
2. **Roll Detection**: Only process cells containing '@' (paper rolls)
3. **Neighbor Counting**: Check all 8 adjacent positions (N, NE, E, SE, S, SW, W, NW)
4. **Accessibility Check**: Roll is accessible if it has < 4 adjacent rolls
5. **Summation**: Count all accessible rolls

**Algorithm:**
```python
def count_accessible_rolls(grid):
    accessible_count = 0
    directions = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            adjacent_rolls = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        adjacent_rolls += 1

            if adjacent_rolls < 4:
                accessible_count += 1

    return accessible_count
```

**Time Complexity**: O(rows × cols × 8) = O(rows × cols) since we check 8 constant neighbors for each cell

## Key Insights

1. **8-Directional Neighbors**: Check all 8 surrounding positions (not just 4 cardinal directions)
2. **Boundary Checking**: Must validate that neighbors are within grid bounds
3. **Accessibility Threshold**: "Fewer than 4" means 0, 1, 2, or 3 adjacent rolls
4. **Empty Spaces**: Only check '@' cells, ignore '.' cells
5. **Example Analysis**:
   - Isolated roll (0 adjacent) → accessible ✓
   - Corner roll in dense area (3 adjacent) → accessible ✓
   - Edge roll surrounded (5 adjacent) → not accessible ✗
   - Center of 3×3 block (8 adjacent) → not accessible ✗

## Test Cases

### Part 1

- **Example from puzzle**: 10×10 grid → 13 accessible rolls
- **Single isolated roll**: 3×3 grid with one roll → 1 accessible
- **3×3 filled grid**: All 9 rolls → 4 accessible (only corners)
- **Horizontal line**: 5 rolls in a row → 5 accessible (max 2 adjacent each)
- **Empty grid**: No rolls → 0 accessible

## Results

**Part 1**: 1433

## Running the Solution

```bash
# Part 1
python3 part_1.py              # Uses input.txt
python3 part_1.py custom.txt   # Uses custom input

# Run tests
python3 test.py
```
