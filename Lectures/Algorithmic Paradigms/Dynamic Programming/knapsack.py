"""
0/1 Knapsack Problem - 2D Dynamic Programming
Based on lecture slide

Problem: Given items with weights and values, select items to maximize
         value without exceeding weight limit W.
         Each item can be used at most once (0/1 constraint).

Recurrence from slide:
    OPT(i,w) = 0                                           if i=0
             = OPT(i-1, w)                                 if w_i > w
             = max{OPT(i-1,w), v_i + OPT(i-1, w-w_i)}     otherwise
"""

class Knapsack:
    def __init__(self, weights, values, capacity):
        """
        Initialize knapsack problem.
        
        Args:
            weights: list of item weights
            values: list of item values
            capacity: maximum weight capacity
        """
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.n = len(weights)
        self.dp = None
    
    def solve_recursive(self, i, w, memo=None):
        """
        Recursive solution with memoization (top-down DP).
        
        OPT(i, w) = maximum value using items 0..i-1 with weight limit w
        
        Args:
            i: considering items 0 through i-1 (i items total)
            w: current weight limit
            memo: memoization dictionary
        """
        if memo is None:
            memo = {}
        
        # ================================================================
        # BASE CASE: No items to consider
        # ================================================================
        if i == 0:
            return 0
        
        # Check memoization
        if (i, w) in memo:
            return memo[(i, w)]
        
        # ================================================================
        # CASE 1: OPT does not select item i (item at index i-1)
        # ================================================================
        # If current item's weight exceeds limit, we MUST skip it
        if self.weights[i-1] > w:
            result = self.solve_recursive(i-1, w, memo)
        
        # ================================================================
        # CASE 2: OPT can choose whether to select item i or not
        # ================================================================
        else:
            # Option A: Don't select item i
            exclude = self.solve_recursive(i-1, w, memo)
            
            # Option B: Select item i
            # New weight limit = w - w_i
            # Add value v_i to the optimal solution of remaining items
            include = self.values[i-1] + self.solve_recursive(i-1, w - self.weights[i-1], memo)
            
            # Take maximum of both options (optimal substructure property)
            result = max(exclude, include)
        
        memo[(i, w)] = result
        return result
    
    def solve_bottom_up(self):
        """
        Bottom-up DP solution (iterative).
        Builds the 2D DP table.
        
        dp[i][w] = OPT(i, w) = max value using first i items with weight limit w
        """
        # Initialize DP table: (n+1) x (capacity+1)
        # dp[i][w] represents using items 0..i-1 with weight limit w
        dp = [[0] * (self.capacity + 1) for _ in range(self.n + 1)]
        
        # Fill the DP table
        for i in range(1, self.n + 1):
            for w in range(self.capacity + 1):
                
                # Item index in arrays (0-indexed)
                item_idx = i - 1
                item_weight = self.weights[item_idx]
                item_value = self.values[item_idx]
                
                # Case 1: Current item's weight exceeds limit
                if item_weight > w:
                    dp[i][w] = dp[i-1][w]
                
                # Case 2: Can choose to include or exclude item
                else:
                    exclude = dp[i-1][w]
                    include = item_value + dp[i-1][w - item_weight]
                    dp[i][w] = max(exclude, include)
        
        self.dp = dp
        return dp[self.n][self.capacity]
    
    def reconstruct_solution(self):
        """
        Reconstruct which items were selected.
        Requires that solve_bottom_up() was called first.
        """
        if self.dp is None:
            self.solve_bottom_up()
        
        selected_items = []
        i = self.n
        w = self.capacity
        
        # Backtrack through the DP table
        while i > 0 and w > 0:
            # Check if value came from including item i
            if self.dp[i][w] != self.dp[i-1][w]:
                # Item i was included
                item_idx = i - 1
                selected_items.append(item_idx)
                w -= self.weights[item_idx]
            i -= 1
        
        selected_items.reverse()
        return selected_items
    
    def print_dp_table(self):
        """Print the DP table for visualization."""
        if self.dp is None:
            self.solve_bottom_up()
        
        print("\nDP Table: dp[i][w] = max value using first i items with weight limit w")
        print("\n     w:", end="")
        for w in range(self.capacity + 1):
            print(f"{w:4}", end="")
        print()
        print("   " + "-" * (5 * (self.capacity + 2)))
        
        for i in range(self.n + 1):
            if i == 0:
                print(f"i={i} |", end="")
            else:
                print(f"i={i} |", end="")
            
            for w in range(self.capacity + 1):
                print(f"{self.dp[i][w]:4}", end="")
            print()


def demonstrate_slide_example():
    """Demonstrate with a clear example."""
    
    print("="*70)
    print("0/1 KNAPSACK PROBLEM - 2D DYNAMIC PROGRAMMING")
    print("="*70)
    
    # Example problem
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 8
    
    print("\nProblem Setup:")
    print(f"Capacity: {capacity}")
    print("\nItems:")
    print("Item | Weight | Value")
    print("-" * 25)
    for i in range(len(weights)):
        print(f"  {i}  |   {weights[i]}    |   {values[i]}")
    print("-" * 25)
    
    knapsack = Knapsack(weights, values, capacity)
    
    # ========================================================================
    # Solution 1: Recursive with memoization
    # ========================================================================
    print("\n" + "="*70)
    print("SOLUTION 1: Recursive (Top-Down with Memoization)")
    print("="*70)
    
    result_recursive = knapsack.solve_recursive(len(weights), capacity)
    print(f"\nMaximum value: {result_recursive}")
    
    # ========================================================================
    # Solution 2: Bottom-up DP
    # ========================================================================
    print("\n" + "="*70)
    print("SOLUTION 2: Bottom-Up DP (Iterative)")
    print("="*70)
    
    result_bottom_up = knapsack.solve_bottom_up()
    print(f"\nMaximum value: {result_bottom_up}")
    
    # Show DP table
    knapsack.print_dp_table()
    
    # Reconstruct solution
    selected = knapsack.reconstruct_solution()
    print(f"\n\nSelected items: {selected}")
    print("\nDetails of selected items:")
    total_weight = 0
    total_value = 0
    for idx in selected:
        print(f"  Item {idx}: weight={weights[idx]}, value={values[idx]}")
        total_weight += weights[idx]
        total_value += values[idx]
    print(f"\nTotal weight: {total_weight}/{capacity}")
    print(f"Total value: {total_value}")


def trace_recursion_example():
    """Show detailed trace of recursion for small example."""
    
    print("\n" + "="*70)
    print("DETAILED RECURSION TRACE")
    print("="*70)
    
    weights = [2, 3]
    values = [3, 4]
    capacity = 5
    
    print("\nSimple example:")
    print(f"Items: weights={weights}, values={values}")
    print(f"Capacity: {capacity}")
    
    def trace_recursive(i, w, depth=0):
        indent = "  " * depth
        
        if i == 0:
            print(f"{indent}OPT({i},{w}) = 0 (base case: no items)")
            return 0
        
        print(f"{indent}OPT({i},{w}): considering item {i-1} (w={weights[i-1]}, v={values[i-1]})")
        
        if weights[i-1] > w:
            print(f"{indent}  Item {i-1} too heavy ({weights[i-1]} > {w}), skip it")
            result = trace_recursive(i-1, w, depth+1)
            print(f"{indent}  OPT({i},{w}) = {result}")
            return result
        else:
            print(f"{indent}  Option A: Exclude item {i-1}")
            exclude = trace_recursive(i-1, w, depth+1)
            
            print(f"{indent}  Option B: Include item {i-1}")
            include = values[i-1] + trace_recursive(i-1, w - weights[i-1], depth+1)
            
            result = max(exclude, include)
            print(f"{indent}  OPT({i},{w}) = max({exclude}, {include}) = {result}")
            return result
    
    print("\nRecursion trace:")
    result = trace_recursive(len(weights), capacity)
    print(f"\nFinal answer: {result}")


def show_recurrence_explanation():
    """Explain the recurrence relation from the slide."""
    
    print("\n" + "="*70)
    print("RECURRENCE RELATION EXPLANATION")
    print("="*70)
    
    print("""
From the lecture slide:

OPT(i, w) = maximum value using first i items with weight limit w

BASE CASE:
    OPT(i, w) = 0                                    if i = 0
    (No items available, value is 0)

CASE 1: OPT does not select item i
    If w_i > w (item too heavy):
        OPT(i, w) = OPT(i-1, w)
        
    We MUST skip this item and use optimal solution with remaining items.

CASE 2: OPT selects item i
    If w_i ≤ w (item can fit):
        OPT(i, w) = max{ OPT(i-1, w),                    [exclude]
                         v_i + OPT(i-1, w - w_i) }       [include]
    
    We choose the BETTER option:
        - Exclude item i: get OPT(i-1, w)
        - Include item i: get v_i + OPT(i-1, w - w_i)
          (add item's value + optimal solution with reduced weight)

OPTIMAL SUBSTRUCTURE PROPERTY:
    The optimal solution for OPT(i, w) depends on optimal solutions
    to smaller subproblems: OPT(i-1, w) and OPT(i-1, w - w_i).
    
    This is why DP works!

2D DP TABLE:
    Rows: items (0 to n)
    Columns: weight limits (0 to W)
    dp[i][w] = OPT(i, w)
""")


def compare_with_1d_coin_change():
    """Compare 2D Knapsack with 1D Coin Change."""
    
    print("\n" + "="*70)
    print("COMPARISON: 2D KNAPSACK vs 1D COIN CHANGE")
    print("="*70)
    
    print("""
KNAPSACK (2D DP):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Problem: Select items to maximize value within weight limit
Constraint: Each item used AT MOST ONCE (0/1 constraint)

DP State: dp[i][w]
    - TWO dimensions: item index AND weight limit
    - dp[i][w] = max value using first i items with weight limit w

Why 2D?
    - Must track WHICH items we've already considered
    - Can't reuse items, so need to know position in item list

Recurrence:
    dp[i][w] = max(dp[i-1][w], v_i + dp[i-1][w-w_i])
                    ↑              ↑
                 exclude        include
             (move to next)  (reduce weight)


COIN CHANGE (1D DP):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Problem: Count ways to make sum using coins
Constraint: Each coin can be used UNLIMITED times

DP State: dp[amount]
    - ONE dimension: only track target amount
    - dp[amount] = number of ways to make amount

Why 1D?
    - Can reuse coins, don't need to track position
    - Only need to know the remaining amount

Recurrence (order doesn't matter):
    dp[amount] += dp[amount - coin]
    Process coins in outer loop to avoid counting orderings


KEY DIFFERENCE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Knapsack: Can't reuse items → Need 2D to track which items used
Coin Change: Can reuse coins → Only need 1D for remaining amount
""")


def main():
    """Run all demonstrations."""
    
    demonstrate_slide_example()
    trace_recursion_example()
    show_recurrence_explanation()
    compare_with_1d_coin_change()
    
    print("\n" + "="*70)
    print("KEY TAKEAWAYS")
    print("="*70)
    print("""
1. Knapsack is 2D DP because:
   - Each item can be used at most once
   - Need to track position in item list
   - State: (item index, weight limit)

2. The recurrence has two cases:
   - Item too heavy: must exclude
   - Item fits: choose max of (exclude, include)

3. Optimal substructure:
   - Solution depends on optimal solutions to subproblems
   - OPT(i,w) uses OPT(i-1,w) and OPT(i-1,w-w_i)

4. Time complexity: O(n*W) where n=items, W=capacity
   Space complexity: O(n*W) for table

5. Can reconstruct solution by backtracking through DP table
""")


if __name__ == "__main__":
    main()