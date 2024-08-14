import os

PLAYER1 = 'X'  # Human player
PLAYER2 = 'O'  # AI player

def minimax(board, is_maximizing):
    if game_over(board):
        return get_score(board)

    if is_maximizing:
        max_eval = float('-inf')
        for move in get_possible_moves(board):
            i, j = move
            board[i][j] = PLAYER2
            eval = minimax(board, False)
            board[i][j] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_possible_moves(board):
            i, j = move
            board[i][j] = PLAYER1
            eval = minimax(board, True)
            board[i][j] = " "
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_move = None
    best_score = float('-inf')
    
    for move in get_possible_moves(board):
        i, j = move
        board[i][j] = PLAYER2
        move_score = minimax(board, False)
        board[i][j] = " "
        if move_score > best_score:
            best_score = move_score
            best_move = move
            
    return best_move

def get_possible_moves(board):
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                possible_moves.append((i, j))
    return possible_moves

def get_score(board):
    if check_winner(board, PLAYER2):
        return 1
    elif check_winner(board, PLAYER1):
        return -1
    elif draw(board):
        return 0

def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    i = 0
    for row in board:
        print("|".join(row))
        i += 1
        if i <= 2:
            print("-" * 5)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] == player) or (board[0][2] == board[1][1] == board[2][0] == player):
        return True
    return False

def draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def available(board, i, j):
    return board[i][j] == " "

def play(board, player):
    while True:
        try:
            i = int(input(f"Player {player}, enter the row position (0-2): "))
            j = int(input(f"Player {player}, enter the column position (0-2): "))
            if 0 <= i < 3 and 0 <= j < 3:
                if available(board, i, j):
                    board[i][j] = player
                    return True
                else:
                    print("This spot is not available. Try again.")
            else:
                print("Invalid input. Please enter a number between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def game_over(board):
    return check_winner(board, PLAYER1) or check_winner(board, PLAYER2) or draw(board)

def game():
    board = create_board()
    print_board(board)
    
    while not game_over(board):
        # Player's turn (Human)
        print(f"Your turn, Player {PLAYER1}:")
        play(board, PLAYER1)
        print_board(board)
        if check_winner(board, PLAYER1):
            print(f"Player {PLAYER1} wins!")
            return
        if draw(board):
            print("It's a draw!")
            return
        
        # AI's turn
        print("AI's turn:")
        move = get_best_move(board)
        if move:
            i, j = move
            board[i][j] = PLAYER2
        print_board(board)
        if check_winner(board, PLAYER2):
            print(f"Player {PLAYER2} (AI) wins!")
            return
        if draw(board):
            print("It's a draw!")
            return

if __name__ == "__main__":
    game()
