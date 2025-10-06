
"""
Pebble Solitaire - State Space Search with Memoization

Problem: Remove as many pebbles as possible by jumping over adjacent pebbles.
Move: oo- becomes --o (or -oo becomes o--)
Goal: Minimize remaining pebbles
"""
def find_all_moves(board):
    """
    Find all valid moves in the current board state.
    
    Returns:
        list of tuples (position, direction)
        direction: 'R' for jump right, 'L' for jump left
    """
    moves = []
    for i in range(23):
        # Pattern: oo- (jump right from position i)
        if i + 2 < len(board):
            if board[i] == 'o' and board[i+1] == 'o' and board[i+2] == '-':
                moves.append((i, 'R'))
            
        # Pattern: -oo (jump left from position i+2)
        if i + 2 < len(board):
            if board[i] == '-' and board[i+1] == 'o' and board[i+2] == 'o':
                moves.append((i, 'L'))

    return moves

    
def apply_move(board, move):
    position, direction = move
    bl = list(board)
    if direction == 'R':
        # oo- becomes --o
        # Position i has first 'o', i+1 has second 'o', i+2 has '-'
        bl[position] = '-'      # Remove first pebble
        bl[position + 1] = '-'  # Remove middle pebble (jumped over)
        bl[position + 2] = 'o'  # Place pebble at destination
    elif direction == 'L':
        bl[position] = 'o'
        bl[position+1] = '-'
        bl[position + 2] = '-'

    return ''.join(bl) 

# def solve(board):
#     # Base case: no moves possible
#     if no_moves_possible(board):
#         return count_pebbles(board)
    
#     # Try all possible moves
#     min_pebbles = infinity
#     for each valid move:
#         new_board = apply_move(board, move)
#         min_pebbles = min(min_pebbles, solve(new_board))
    
#     return min_pebbles

def solve(board, memo):
    """
    Find minimum number of pebbles remaining.
    
    Args:
        board: string of '-' and 'o' representing the board
        memo: dictionary to cache results
    
    Returns:
        minimum number of pebbles that can remain
    """

    if board in memo:
        return memo[board]
    
    # Find all possible moves from current state
    moves = find_all_moves(board)

    # Base case: no moves possible
    if not moves:
        result = board.count('o')
        memo[board] = result # key is the board 
        return result
    
    # Try all possible moves and find minimum
    min_pebbles = 23
    for move in moves:
        new_board = apply_move(board, move)
        min_pebbles = min(min_pebbles, solve(new_board, memo))

    memo[board] = min_pebbles
    return min_pebbles




if __name__ == "__main__":
    n = int(input())    
    for _ in range(n):
        board = input().strip()
        print(solve(board, {}))


   

