print("LET'S PLAY TIC TAC TOE!\n")

def display_board(board):
    print("*************")
    for row in board:
        print("* " + " | ".join(row) + " *")
        print("*************")

def player_input(player):
    while True:
        try:
            user_input = input(f"Player {player}, enter row and column (0-2) or 'q' to quit: ")
            if user_input.lower() == 'q':
                print("Game aborted. Thanks for playing!")
                exit()
            row, col = map(int, user_input.split())
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("That spot is already taken. Try again.")
        except (IndexError, ValueError):
            print("Invalid input. Please enter row and column as numbers between 0 and 2, or 'q' to quit.")

def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def play():
    global board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    for _ in range(9):
        display_board(board)
        player_input(players[turn])
        if check_win(board, players[turn]):
            display_board(board)
            print(f"Player {players[turn]} wins!")
            return
        turn = 1 - turn
    
    display_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    play()