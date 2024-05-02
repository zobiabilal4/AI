import random

def initialize_board():
    board = [" " for _ in range(9)]
    return board

def display_board(board):
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def check_tie(board):
    return " " not in board

# Minimax algorithm with Alpha-Beta pruning
def minimax(board, depth, maximizing_player):
    if check_win(board, "X"):
        return -10 + depth
    if check_win(board, "O"):
        return 10 - depth
    if check_tie(board):
        return 0

    if maximizing_player:
        max_eval = float("-inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, depth + 1, False)
                board[i] = " "
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth + 1, True)
                board[i] = " "
                min_eval = min(min_eval, eval)
        return min_eval

# Find the best move for the computer using the minimax algorithm
def best_move(board):
    best_eval = float("-inf")
    best_move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            move_eval = minimax(board, 0, False)
            board[i] = " "

            if move_eval > best_eval:
                best_eval = move_eval
                best_move = i

    return best_move

# Main game loop
def play_game():
    board = initialize_board()
    display_board(board)

    while True:
        player_move = int(input("Enter your move (1-9): ")) - 1

        if board[player_move] == " " and 0 <= player_move <= 8:
            board[player_move] = "X"
            display_board(board)

            if check_win(board, "X"):
                print("You win!")
                break
            if check_tie(board):
                print("It's a tie!")
                break

            computer_move = best_move(board)
            board[computer_move] = "O"
            print(f"Computer's move: {computer_move + 1}")
            display_board(board)

            if check_win(board, "O"):
                print("Computer wins!")
                break
            if check_tie(board):
                print("It's a tie!")
                break

        else:
            print("Invalid move. Try again.")

def main():
    play_game()
main()
