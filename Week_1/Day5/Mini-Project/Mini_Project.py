# Tic Tac Toe - (X et O)

def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def display_board(board):
    print("\nTIC TAC TOE")
    print("+" + "---+" * 3)
    for i in range(3):
        print("| " + " | ".join(board[i]) + " |")
        print("+" + "---+" * 3)
    print()  # ligne vide

def player_input(board, player):
    
    while True:
        try:
            raw_row = input(f"Player {player} — enter row (1-3): ").strip()
            raw_col = input(f"Player {player} — enter column (1-3): ").strip()

            row = int(raw_row) - 1
            col = int(raw_col) - 1

            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid position: row and column must be 1, 2 or 3. Réessaie.\n")
                continue

            if board[row][col] != " ":
                print("Cell already taken. Choose another.\n")
                continue

            board[row][col] = player
            break

        except ValueError:
            print("Invalid input: please enter numbers only (1, 2 or 3). Réessaie.\n")

def check_win(board, player):
    # lignes
    for r in range(3):
        if all(cell == player for cell in board[r]):
            return True

    # colonnes
    for c in range(3):
        if all(board[r][c] == player for r in range(3)):
            return True

    # diagonales
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_tie(board):
    return all(cell != " " for row in board for cell in row)

def switch_player(current):
    return "O" if current == "X" else "X"

def play():
    board = create_board()
    current_player = "X"  # X commence
    winner = None

    while True:
        display_board(board)
        player_input(board, current_player)

        if check_win(board, current_player):
            winner = current_player
            break

        if check_tie(board):
            break

        current_player = switch_player(current_player)

    display_board(board)
    if winner:
        print(f"Player {winner} wins! Félicitations !")
    else:
        print("Match nul !")

if __name__ == "__main__":
    play()
