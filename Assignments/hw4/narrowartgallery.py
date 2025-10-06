"""
Setup:

Gallery has N rows × 2 columns = 2N rooms total
Each room has a value
Must close exactly k rooms
Visitors enter from one end, exit from the other end

Constraints (can't close these combinations):

Two rooms in the same row (blocks horizontal passage)
Two diagonally adjacent rooms (blocks diagonal passage)

Goal:
Close k rooms to maximize the total value of remaining open rooms.
Input:

Line 1: N (rows), k (rooms to close)
Next N lines: two integers (values of left and right room in that row)
End: "0 0"

Output:
Maximum total value of open rooms after closing k rooms optimally.
Key Insight
This is the opposite of a typical optimization: instead of "select k items to maximize value," you're "exclude k items to maximize remaining value."
Total value available - Value of closed rooms = Value of open rooms
So maximize: sum(all rooms) - sum(k closed rooms)
Which means: minimize the value of k closed rooms you select
Constraints translate to:

Can't close both rooms in same row
Can't close diagonally adjacent rooms (room[i][0] and room[i+1][1], or room[i][1] and room[i-1][0])

This is a 2D DP problem similar to knapsack but with adjacency constraints.

"""

def solve(row, k, last_closed, memo):
    """
    Top-down DP with memoization.
    
    Args:
        row: current row index (0 to N-1)
        k: number of rooms still need to close
        last_closed: what was closed in previous row
                     0 = nothing, 1 = left, 2 = right
        memo: memoization dictionary
    
    Returns:
        minimum value of k rooms we close
    """
    # Base case: processed all rows
    if row == N:
        if k == 0:
            return 0  # Successfully closed exactly k rooms
    
    # Check memo
    if (row, k, last_closed) in memo:
        return memo[(row, k, last_closed)]
    
    # Try all valid options for current row
    options = []
    
    # Option 1: Close nothing in this row
    if k >= 0:  # Can skip if we still have rooms to close later
        options.append(solve(row + 1, k, 0, memo))
    
    # Option 2: Close left room
    # Can't close if last row closed right (diagonal)
    if last_closed != 2:
        options.append(values[row][0] + solve(row + 1, k - 1, 1, memo))
    
    # Option 3: Close right room
    # Can't close if last row closed left (diagonal)
    if last_closed != 1:
        options.append(values[row][1] + solve(row + 1, k - 1, 2, memo))
    
    # Can't close both rooms in same row (violates constraint)
    
    result = min(options)
    memo[(row, k, last_closed)] = result
    return result


# Main
total_value = sum(sum(row) for row in values)
min_closed_value = solve(0, k, 0, {})
max_open_value = total_value - min_closed_value
print(max_open_value)