# Day 8: Playground

## Problem Summary

The challenge involves connecting junction boxes suspended in 3D space using string lights. The goal is to determine which junction boxes to connect so that electricity can flow between them, forming circuits.

**Part 1:** After connecting the 1000 closest pairs of junction boxes (by Euclidean distance), multiply together the sizes of the three largest circuits.

## Solution Approach

### Part 1: [part_1.py](part_1.py)

This problem is essentially a graph clustering problem where we need to:

1. **Parse 3D coordinates** from the input (X,Y,Z format)
2. **Calculate pairwise distances** between all junction boxes using Euclidean distance: `sqrt((x2-x1)² + (y2-y1)² + (z2-z1)²)`
3. **Sort pairs by distance** to identify the closest pairs
4. **Process the shortest pairs** using a Union-Find (Disjoint Set) data structure to track which boxes belong to the same circuit
5. **Count circuit sizes** and find the three largest

**Key Data Structure:** Union-Find with path compression and union by rank for efficient merging of circuits.

**Algorithm:**
- Start with each junction box as its own circuit
- Process the 1000 shortest pairs in order
- For each pair, merge their circuits (if not already merged)
- After processing all pairs, extract circuit sizes
- Return the product of the three largest circuits

**Important Detail:** The problem asks us to process the 1000 shortest *pairs* (by distance), not to make 1000 successful connections. Some pairs may already be in the same circuit, in which case the union operation doesn't change anything, but we still count it as one of the 1000 pairs processed.

## Key Insights

1. **Union-Find is ideal** for tracking connected components efficiently
2. **Euclidean distance in 3D** is straightforward: sqrt of sum of squared differences
3. **Sorting all pairs** is O(n²log n) but necessary to process in distance order
4. **Path compression and union by rank** optimize the Union-Find operations to nearly O(1)
5. **Counting vs attempting:** We process 1000 pairs, not make 1000 successful connections

## Test Cases

### Example from puzzle description:
- 20 junction boxes
- Process 10 shortest pairs
- Results in 11 circuits: [5, 4, 2, 2, 1, 1, 1, 1, 1, 1, 1]
- Product of three largest: 5 × 4 × 2 = **40** ✓

## Results

**Part 1:** `352584`

## Running Instructions

```bash
# Run Part 1
python3 part_1.py

# Run with custom input
python3 part_1.py custom.txt

# Run tests
python3 test.py

# Using mise tasks
mise run solve 8 1
mise run test 8
```
