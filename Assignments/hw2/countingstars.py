import sys
sys.setrecursionlimit(10000)

def dfs(grid, r, c, R, C):
    if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] != '-':
        return
    grid[r][c] = '#'  # mark visited
    dfs(grid, r+1, c, R, C)
    dfs(grid, r-1, c, R, C)
    dfs(grid, r, c+1, R, C)
    dfs(grid, r, c-1, R, C)

lines = [line.strip() for line in sys.stdin if line.strip() != '']
i = 0
case = 1

while i < len(lines):
    # first number = rows, second = columns
    rows, cols = map(int, lines[i].split())
    i += 1

    grid = [list(lines[i + r]) for r in range(rows)]
    i += rows

    stars = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '-':
                stars += 1
                dfs(grid, r, c, rows, cols)

    print(f"Case {case}: {stars}")
    case += 1
