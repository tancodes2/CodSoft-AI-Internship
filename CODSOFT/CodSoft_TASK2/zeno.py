import math
import time

player_symbol = ''
ai_symbol = ''
ai_name = 'Zeno'
score = {'You': 0, ai_name: 0, 'Draws': 0}

def print_board(board):
    print("\nCurrent Board:")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print()

def check_winner(board, player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

def is_board_full(board):
    return all(cell != '-' for cell in board)

def minimax_alpha_beta(board, depth, alpha, beta, maximizing):
    if check_winner(board, ai_symbol):
        return 1
    elif check_winner(board, player_symbol):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == '-':
                board[i] = ai_symbol
                eval = minimax_alpha_beta(board, depth + 1, alpha, beta, False)
                board[i] = '-'
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == '-':
                board[i] = player_symbol
                eval = minimax_alpha_beta(board, depth + 1, alpha, beta, True)
                board[i] = '-'
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def find_best_move(board):
    best_move = -1
    best_eval = -math.inf
    for i in range(9):
        if board[i] == '-':
            board[i] = ai_symbol
            eval = minimax_alpha_beta(board, 0, -math.inf, math.inf, False)
            board[i] = '-'
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

def choose_symbol():
    global player_symbol, ai_symbol
    while True:
        choice = input("Choose your symbol (X/O): ").strip().upper()
        if choice in ['X', 'O']:
            player_symbol = choice
            ai_symbol = 'O' if choice == 'X' else 'X'
            break
        else:
            print("Invalid choice. Please choose X or O.")

def play_game():
    global score
    board = ['-'] * 9
    print("\nLet's play Tic-Tac-Toe!")
    print("You vs", ai_name)
    print("Use numbers 0-8 to choose a cell as shown:")
    print(" 0 | 1 | 2\n---+---+---\n 3 | 4 | 5\n---+---+---\n 6 | 7 | 8")

    while True:
        print_board(board)
        try:
            move = int(input("Your move (0-8): "))
            if move < 0 or move > 8 or board[move] != '-':
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Please enter a number between 0 and 8.")
            continue

        board[move] = player_symbol
        if check_winner(board, player_symbol):
            print_board(board)
            print("You win!🎉")
            score['You'] += 1
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!🤝")
            score['Draws'] += 1
            break

        print(f"{ai_name} is thinking...")
        time.sleep(1)
        ai_move = find_best_move(board)
        board[ai_move] = ai_symbol

        if check_winner(board, ai_symbol):
            print_board(board)
            print(f"💻 {ai_name} wins! Better luck next time.")
            score[ai_name] += 1
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!🤝")
            score['Draws'] += 1
            break

def show_scores():
    print("\nCurrent Scoreboard:")
    print(f"You: {score['You']}  |  {ai_name}: {score[ai_name]}  |  Draws: {score['Draws']}\n")

def main():
    print("🎮 Welcome to Tic-Tac-Toe!")
    choose_symbol()
    while True:
        play_game()
        show_scores()
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! See you next time 👋")
            break

main()