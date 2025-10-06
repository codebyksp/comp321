class NQueensBacktracking:
    """
    N-Queens solver using recursive backtracking.
    Based on the PlaceQueens algorithm from lecture.
    
    Key concepts from lecture:
    - Q[1..n] array where Q[i] = column position of queen in row i
    - r = index of first empty row
    - Q[1..r-1] = positions of first r-1 queens already placed
    """
    
    def __init__(self, n=8):
        self.n = n
        self.Q = [0] * (n + 1)  # 1-indexed array (Q[0] unused, Q[1..n] used)
        self.solutions = []
        self.recursive_calls = 0
        self.legality_checks = 0
        
    def place_queens(self, r, verbose=False):
        """
        PlaceQueens(Q[1..n], r) from lecture
        
        Args:
            r: index of first empty row (1-indexed)
            verbose: if True, print each step
        """
        self.recursive_calls += 1
        
        if verbose:
            indent = "  " * (r - 1)
            print(f"{indent}PlaceQueens called with r={r}, Q={self.Q[1:r]}")
        
        # Base case: if r == n + 1, all queens placed successfully
        if r == self.n + 1:
            if verbose:
                print(f"{'  ' * (r-1)}✓ Solution found: {self.Q[1:]}")
            self.solutions.append(self.Q[1:self.n + 1].copy())
            return
        
        # Recursive case: try all possible placements of queen on row r
        # For j ← 1 to n
        for j in range(1, self.n + 1):
            if verbose:
                print(f"{'  ' * (r-1)}Trying queen at row {r}, column {j}")
            
            # Check if placement is legal
            legal = True
            
            # For i ← 1 to r-1: check against all previously placed queens
            for i in range(1, r):
                self.legality_checks += 1
                
                # Check three conditions from lecture:
                # 1. Q[i] = j → same column
                # 2. Q[i] = j + r - i → diagonal /
                # 3. Q[i] = j - r + i → diagonal \
                if (self.Q[i] == j or 
                    self.Q[i] == j + r - i or 
                    self.Q[i] == j - r + i):
                    legal = False
                    if verbose:
                        print(f"{'  ' * (r-1)}  ✗ Conflicts with queen at row {i}, col {self.Q[i]}")
                    break
            
            # If legal, place queen and recurse
            if legal:
                if verbose:
                    print(f"{'  ' * (r-1)}  ✓ Legal! Placing queen and recursing...")
                
                # Q[r] ← j
                self.Q[r] = j
                
                # PlaceQueens(Q[1..n], r + 1) - RECURSION!
                self.place_queens(r + 1, verbose)
                
                # Implicit backtracking: when recursion returns, we try next j
                if verbose:
                    print(f"{'  ' * (r-1)}  ← Backtracked from r={r+1}")
    
    def solve(self, verbose=False):
        """Solve the N-Queens problem starting from row 1."""
        print(f"{'='*70}")
        print(f"Solving {self.n}-Queens Problem using Recursive Backtracking")
        print(f"{'='*70}\n")
        
        if verbose:
            print("=== DETAILED EXECUTION TRACE ===\n")
        
        # Start with row 1 (first empty row)
        self.place_queens(1, verbose)
        
        print(f"\n{'='*70}")
        print(f"RESULTS")
        print(f"{'='*70}")
        print(f"✓ Solutions found: {len(self.solutions)}")
        print(f"✓ Recursive calls: {self.recursive_calls:,}")
        print(f"✓ Legality checks: {self.legality_checks:,}")
        print(f"\n{'='*70}")
        print(f"SEARCH SPACE ANALYSIS")
        print(f"{'='*70}")
        print(f"Naive approach: C({self.n}²,{self.n}) = C({self.n**2},{self.n}) = {self.combinations(self.n**2, self.n):,}")
        print(f"One-per-row approach: {self.n}^{self.n} = {self.n**self.n:,}")
        print(f"Actual recursive calls: {self.recursive_calls:,}")
        reduction = (1 - self.recursive_calls / self.n**self.n) * 100
        print(f"Reduction from pruning: {reduction:.2f}%")
        
        return self.solutions
    
    def combinations(self, n, k):
        """Calculate C(n,k) = n!/(k!(n-k)!)"""
        if k > n or k < 0:
            return 0
        if k == 0 or k == n:
            return 1
        
        result = 1
        for i in range(min(k, n - k)):
            result = result * (n - i) // (i + 1)
        return result
    
    def print_solution(self, solution_index=0):
        """Print a visual board for a specific solution."""
        if not self.solutions or solution_index >= len(self.solutions):
            print("No solution to display")
            return
        
        sol = self.solutions[solution_index]
        print(f"\nSolution {solution_index + 1}: Q = {sol}")
        print(f"(Q[i] = column where queen is placed in row i)\n")
        
        # Print column numbers
        print("    ", end="")
        for col in range(1, self.n + 1):
            print(f" {col} ", end="")
        print("\n   " + "─" * (self.n * 3 + 1))
        
        # Print board (1-indexed)
        for row in range(1, self.n + 1):
            print(f"{row} │", end="")
            for col in range(1, self.n + 1):
                if sol[row - 1] == col:
                    print(" ♛", end="")
                else:
                    print(" ·", end="")
            print(" │")
        
        print("   " + "─" * (self.n * 3 + 1))
    
    def explain_diagonal_check(self):
        """Explain the diagonal check formulas from lecture."""
        print("\n" + "="*70)
        print("UNDERSTANDING THE DIAGONAL CHECKS")
        print("="*70)
        print("""
From lecture, a queen at (i, Q[i]) conflicts with a queen at (r, j) if:

1. Q[i] = j 
   → Same column (vertical attack)

2. Q[i] = j + r - i
   → Same / diagonal (going up-right)
   → The difference in rows equals difference in columns
   → |i - r| = |Q[i] - j| and Q[i] > j
   
3. Q[i] = j - r + i
   → Same \\ diagonal (going up-left)
   → The difference in rows equals difference in columns
   → |i - r| = |Q[i] - j| and Q[i] < j

Example: If we have a queen at row 3, column 5, and we're checking row 6, column 2:
- i=3, Q[i]=5
- r=6, j=2
- Check 2: Q[i] = j + r - i → 5 = 2 + 6 - 3 → 5 = 5 ✓ CONFLICT!
  (They are on the same / diagonal)
""")


def demonstrate_4queens_verbose():
    """Show detailed execution trace for 4-Queens."""
    print("\n" + "="*70)
    print("DEMONSTRATION: 4-Queens with Verbose Tracing")
    print("="*70)
    print("\nWatch how the algorithm:")
    print("  1. Tries placing queens column by column in each row")
    print("  2. Checks legality against previously placed queens")
    print("  3. Backtracks when no legal placement exists")
    print("  4. Recursively solves for the next row when legal\n")
    
    solver = NQueensBacktracking(4)
    solver.solve(verbose=True)
    
    print("\nAll solutions found:")
    for i in range(len(solver.solutions)):
        solver.print_solution(i)


def demonstrate_8queens():
    """Solve classic 8-Queens problem."""
    print("\n" + "="*70)
    print("CLASSIC 8-QUEENS PROBLEM")
    print("="*70)
    
    solver = NQueensBacktracking(8)
    solutions = solver.solve(verbose=False)
    
    # Show first few solutions
    print("\nFirst 3 solutions:")
    for i in range(min(3, len(solutions))):
        solver.print_solution(i)
    
    # Explain the diagonal logic
    solver.explain_diagonal_check()


# Main execution
if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════════════════════════╗
║           N-QUEENS RECURSIVE BACKTRACKING                          ║
║           Based on Lecture Algorithm                               ║
╚════════════════════════════════════════════════════════════════════╝

This implementation follows the PlaceQueens(Q[1..n], r) algorithm:
  • Q[1..n]: array where Q[i] = column of queen in row i
  • r: index of first empty row
  • Base case: r = n+1 (all queens placed)
  • Recursive case: try each column j, check legality, recurse
""")
    
    # Small example with full trace
    demonstrate_4queens_verbose()
    
    # Classic 8-Queens
    demonstrate_8queens()
    
    print("\n" + "="*70)
    print("KEY TAKEAWAYS")
    print("="*70)
    print("""
1. REPRESENTATION:
   - Use 1D array Q where Q[i] = column of queen in row i
   - This enforces "one queen per row" constraint automatically

2. LEGALITY CHECK:
   - Only check against queens in rows 1..r-1 (already placed)
   - Three conditions: same column, same / diagonal, same \\ diagonal

3. BACKTRACKING:
   - When recursion returns, we automatically try next column
   - This "backs up" to previous decision point when stuck

4. PRUNING:
   - Don't explore subtrees from illegal placements
   - Reduces 16M possibilities to ~15K actual checks for 8-Queens!
""")