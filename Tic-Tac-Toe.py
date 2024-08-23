# Constants for the players
HUMAN = 'X'
AI = 'O'
EMPTY = '_'

# Function to check for available moves
def is_moves_left(board):
    return any(EMPTY in row for row in board)

# Function to evaluate the current state of the board
def evaluate(board):
    # Check rows for a win
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return 10 if row[0] == AI else -10

    # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return 10 if board[0][col] == AI else -10

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return 10 if board[0][0] == AI else -10
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return 10 if board[0][2] == AI else -10

    # If no one wins
    return 0

# Minimax function to find the best move
def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    # If the AI has won
    if score == 10:
        return score - depth  # Encourage faster wins
    # If the human has won
    if score == -10:
        return score + depth  # Discourage slower losses
    # If no more moves and no winner (tie)
    if not is_moves_left(board):
        return 0

    # If it's AI's turn (Maximizing player)
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    best_score = max(best_score, minimax(board, depth + 1, False))
                    board[i][j] = EMPTY
        return best_score

    # If it's Human's turn (Minimizing player)
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    best_score = min(best_score, minimax(board, depth + 1, True))
                    board[i][j] = EMPTY
        return best_score

# Function to find the best possible move for the AI
def find_best_move(board):
    best_move = (-1, -1)
    best_value = -float('inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                move_value = minimax(board, 0, False)
                board[i][j] = EMPTY

                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)

    return best_move

# Function to print the current board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Example usage
if __name__ == "__main__":
    # Initial board state
    board = [
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['_', '_', '_']
    ]

    print("Initial board:")
    print_board(board)

    best_move = find_best_move(board)

    print("\nOptimal Move for AI:")
    print(f"Row: {best_move[0]}, Column: {best_move[1]}")

    # Apply the best move to the board
    board[best_move[0]][best_move[1]] = AI
    print("\nUpdated board after AI's move:")
    print_board(board)
