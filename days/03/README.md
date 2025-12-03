# Day 3: Lobby

## Problem Summary

The puzzle involves finding maximum joltage from battery banks to power an escalator.

- **Part 1**: Each bank is a string of digits (1-9). Select exactly 2 batteries to form a 2-digit number. Find the maximum possible for each bank and sum them.
- **Part 2**: Now select exactly 12 batteries to form a 12-digit number. Find the maximum possible for each bank and sum them.

## Solution Approach

### Part 1 ([part_1.py](part_1.py))

The solution tries all possible pairs of batteries in each bank:

1. **Pair Generation**: For each bank, generate all pairs (i, j) where i < j
2. **Joltage Calculation**: Form a 2-digit number by concatenating digits at positions i and j
3. **Maximum Selection**: Find the maximum joltage from all pairs
4. **Summation**: Sum the maximum joltages from all banks

**Algorithm:**
```python
def find_max_joltage(bank):
    max_joltage = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)
    return max_joltage
```

**Key Insight**: We can pick ANY two batteries from the bank, not just consecutive ones. The order is preserved (can't rearrange), so picking batteries at positions i and j (i < j) gives us the digit at position i followed by the digit at position j.

**Time Complexity**: O(n × m²) where n is the number of banks and m is the average length of each bank

### Part 2 ([part_2.py](part_2.py))

Part 2 uses a greedy algorithm to select exactly 12 batteries that form the maximum 12-digit number:

1. **Greedy Selection**: At each step, select the battery with the maximum digit that still leaves enough positions for remaining selections
2. **Position Constraints**: When selecting position i (0-indexed), ensure there are at least (12 - i - 1) positions remaining
3. **Sequential Building**: Build the 12-digit number one digit at a time, always choosing the best available option

**Algorithm:**
```python
def find_max_joltage_12(bank):
    selected_indices = []
    remaining_to_select = 12
    start_pos = 0

    for i in range(12):
        remaining_after = remaining_to_select - 1
        max_digit = -1
        max_pos = start_pos

        # Select from [start_pos, len(bank) - remaining_after]
        for pos in range(start_pos, len(bank) - remaining_after):
            digit = int(bank[pos])
            if digit > max_digit:
                max_digit = digit
                max_pos = pos

        selected_indices.append(max_pos)
        start_pos = max_pos + 1
        remaining_to_select -= 1

    return int(''.join(bank[i] for i in selected_indices))
```

**Key Insight**: The greedy approach works because we're building the number from left to right (most significant digit first). At each position, choosing the maximum available digit that leaves enough positions for the remaining digits guarantees the maximum overall number.

**Time Complexity**: O(n × m × k) where n is the number of banks, m is the average length, and k is the number of batteries to select (12)

## Key Insights

1. **Order Preservation**: Batteries cannot be rearranged - if we pick positions i and j, the result is digits[i] + digits[j]
2. **Non-Consecutive Selection**: We can pick any batteries, not just adjacent ones
3. **Greedy Strategy (Part 2)**: Building from left to right and choosing the maximum at each step (with constraints) gives the optimal result
4. **Examples (Part 1)**:
   - `987654321111111` → Pick positions 0,1 → `98`
   - `811111111111119` → Pick positions 0,14 → `89` (8 at start, 9 at end)
   - `234234234234278` → Pick positions 12,13 → `78` (last two digits)
   - `818181911112111` → Pick positions 6,7 → `92` (9 and 2 from middle)
5. **Examples (Part 2)**:
   - `987654321111111` → `987654321111` (all except last 3 ones)
   - `811111111111119` → `811111111119` (skip some middle 1s)
   - `234234234234278` → `434234234278` (skip early 2,3,2)
   - `818181911112111` → `888911112111` (skip early 1s)

## Test Cases

### Part 1

- **Example from puzzle**: 4 banks → sum = 357
  - `987654321111111` → 98
  - `811111111111119` → 89
  - `234234234234278` → 78
  - `818181911112111` → 92
- **Single bank**: `987654321` → 98
- **All same digits**: `11111` → 11, `99999` → 99
- **Ascending/Descending**: `123456789` → 89, `987654321` → 98

### Part 2

- **Example from puzzle**: 4 banks → sum = 3,121,910,778,619
  - `987654321111111` → 987654321111
  - `811111111111119` → 811111111119
  - `234234234234278` → 434234234278
  - `818181911112111` → 888911112111
- **All same digits**: `111111111111` → 111111111111, `999999999999` → 999999999999
- **Descending sequence**: `987654321987654` → 987654987654 (greedy picks best at each position)

## Results

**Part 1**: 17443
**Part 2**: 172167155440541

## Running the Solution

```bash
# Part 1
python3 part_1.py              # Uses input.txt
python3 part_1.py custom.txt   # Uses custom input

# Part 2
python3 part_2.py              # Uses input.txt
python3 part_2.py custom.txt   # Uses custom input

# Run tests
python3 test.py
```
