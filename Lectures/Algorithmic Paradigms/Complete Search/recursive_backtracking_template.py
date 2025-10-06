"""
Recursive Backtracking Template
Based on lecture slide - general pattern for solving constraint satisfaction problems
"""

def backtrack(state):
    """
    Generic recursive backtracking template.
    
    Args:
        state: Current state/configuration of the problem
        
    Returns:
        True if solution found, False otherwise
    """
    
    # BASE CASE: If at a solution, report success
    if is_solution(state):
        process_solution(state)
        return True  # or False if you want to find ALL solutions
    
    # RECURSIVE CASE: Try all possible choices from current state
    for choice in get_choices(state):
        
        # ① Make that choice and take one step along path
        make_choice(state, choice)
        
        # ② Use recursion to try to solve the problem for the new node/state
        if backtrack(state):
            # ③ If the recursive call succeeds, report success to previous level
            return True
        
        # ④ Back out of the current choice to restore state at beginning of loop
        unmake_choice(state, choice)
    
    # If no choice led to solution, report failure
    return False


# ============================================================================
# Helper functions to implement for your specific problem
# ============================================================================

def is_solution(state):
    """
    Check if current state is a complete solution.
    
    Examples:
    - N-Queens: All N queens placed
    - Sudoku: All cells filled
    - Maze: Reached the exit
    """
    pass


def process_solution(state):
    """
    Do something with the solution (print it, save it, etc.)
    """
    print(f"Solution found: {state}")


def get_choices(state):
    """
    Return list of all possible choices/moves from current state.
    
    Examples:
    - N-Queens: All columns in current row
    - Sudoku: All numbers 1-9 for current empty cell
    - Maze: All adjacent unvisited cells
    """
    return []


def make_choice(state, choice):
    """
    Modify state to reflect making this choice.
    Take one step along the path.
    
    Examples:
    - N-Queens: Place queen at position
    - Sudoku: Fill cell with number
    - Maze: Mark cell as visited, add to path
    """
    pass


def unmake_choice(state, choice):
    """
    Undo the choice to restore state.
    This is the "backtracking" part!
    
    Examples:
    - N-Queens: Remove queen from position
    - Sudoku: Clear cell
    - Maze: Unmark cell, remove from path
    """
    pass


# ============================================================================
# Example 1: N-Queens Problem
# ============================================================================

class NQueensBacktrack:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n  # board[row] = column of queen
        self.solutions = []
    
    def solve(self):
        self.backtrack(0)
        return self.solutions
    
    def backtrack(self, row):
        """Place queens row by row."""
        # Base case: placed all queens
        if row == self.n:
            self.solutions.append(self.board[:])
            return False  # Continue searching for more solutions
        
        # Try each column in this row
        for col in range(self.n):
            if self.is_safe(row, col):
                # Make choice
                self.board[row] = col
                
                # Recurse
                if self.backtrack(row + 1):
                    return True
                
                # Unmake choice (backtrack)
                self.board[row] = -1
        
        return False
    
    def is_safe(self, row, col):
        """Check if placing queen at (row, col) is valid."""
        for prev_row in range(row):
            prev_col = self.board[prev_row]
            if prev_col == col or abs(prev_row - row) == abs(prev_col - col):
                return False
        return True


# ============================================================================
# Example 2: Subset Sum Problem
# ============================================================================

class SubsetSumBacktrack:
    """Find all subsets of numbers that sum to target."""
    
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target
        self.solutions = []
        self.current_subset = []
        self.current_sum = 0
    
    def solve(self):
        self.backtrack(0)
        return self.solutions
    
    def backtrack(self, index):
        """Try including/excluding each number."""
        # Base case: found a solution
        if self.current_sum == self.target:
            self.solutions.append(self.current_subset[:])
            return
        
        # Base case: explored all numbers or exceeded target
        if index >= len(self.numbers) or self.current_sum > self.target:
            return
        
        # Choice 1: Include current number
        self.current_subset.append(self.numbers[index])
        self.current_sum += self.numbers[index]
        self.backtrack(index + 1)
        # Backtrack
        self.current_subset.pop()
        self.current_sum -= self.numbers[index]
        
        # Choice 2: Exclude current number
        self.backtrack(index + 1)


# ============================================================================
# Example 3: Maze Solver
# ============================================================================

class MazeSolver:
    """Find path through maze using backtracking."""
    
    def __init__(self, maze, start, end):
        self.maze = maze  # 2D array: 0=open, 1=wall
        self.start = start
        self.end = end
        self.path = []
        self.visited = set()
    
    def solve(self):
        if self.backtrack(self.start):
            return self.path
        return None
    
    def backtrack(self, pos):
        """Try to find path from current position to end."""
        row, col = pos
        
        # Base case: reached end
        if pos == self.end:
            self.path.append(pos)
            return True
        
        # Check if valid position
        if not self.is_valid(pos):
            return False
        
        # Make choice: visit this cell
        self.visited.add(pos)
        self.path.append(pos)
        
        # Try all four directions
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_pos = (row + dr, col + dc)
            if self.backtrack(next_pos):
                return True
        
        # Backtrack: unvisit this cell
        self.path.pop()
        self.visited.remove(pos)
        
        return False
    
    def is_valid(self, pos):
        """Check if position is valid and unvisited."""
        row, col = pos
        if row < 0 or row >= len(self.maze):
            return False
        if col < 0 or col >= len(self.maze[0]):
            return False
        if self.maze[row][col] == 1:  # Wall
            return False
        if pos in self.visited:
            return False
        return True


# ============================================================================
# Example 4: Generate All Permutations
# ============================================================================

class PermutationGenerator:
    """Generate all permutations of a list."""
    
    def __init__(self, items):
        self.items = items
        self.permutations = []
        self.current = []
        self.used = [False] * len(items)
    
    def generate(self):
        self.backtrack()
        return self.permutations
    
    def backtrack(self):
        """Build permutations one element at a time."""
        # Base case: built complete permutation
        if len(self.current) == len(self.items):
            self.permutations.append(self.current[:])
            return
        
        # Try each unused item
        for i in range(len(self.items)):
            if not self.used[i]:
                # Make choice
                self.current.append(self.items[i])
                self.used[i] = True
                
                # Recurse
                self.backtrack()
                
                # Backtrack
                self.current.pop()
                self.used[i] = False


# ============================================================================
# Testing the examples
# ============================================================================

if __name__ == "__main__":
    print("="*70)
    print("RECURSIVE BACKTRACKING TEMPLATE EXAMPLES")
    print("="*70)
    
    # Example 1: N-Queens
    print("\n1. N-Queens (4x4):")
    queens = NQueensBacktrack(4)
    solutions = queens.solve()
    print(f"   Found {len(solutions)} solutions")
    print(f"   First solution: {solutions[0]}")
    
    # Example 2: Subset Sum
    print("\n2. Subset Sum ([1,2,3,4,5], target=7):")
    subset = SubsetSumBacktrack([1, 2, 3, 4, 5], 7)
    solutions = subset.solve()
    print(f"   Found {len(solutions)} solutions")
    for sol in solutions:
        print(f"   {sol} -> sum = {sum(sol)}")
    
    # Example 3: Maze
    print("\n3. Maze Solver:")
    maze = [
        [0, 0, 1, 0],
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    solver = MazeSolver(maze, (0, 0), (3, 3))
    path = solver.solve()
    print(f"   Path found: {path}")
    
    # Example 4: Permutations
    print("\n4. Permutations of [1,2,3]:")
    perm = PermutationGenerator([1, 2, 3])
    perms = perm.generate()
    print(f"   Found {len(perms)} permutations")
    for p in perms:
        print(f"   {p}")
    
    print("\n" + "="*70)
    print("KEY PATTERN:")
    print("="*70)
    print("""
    1. Check if at solution → report success
    2. For each possible choice:
        a. Make the choice
        b. Recurse to solve subproblem
        c. If successful, report success up
        d. Unmake choice (backtrack)
    3. If no choice works → report failure
    """)