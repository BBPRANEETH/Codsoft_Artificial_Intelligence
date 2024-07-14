def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()

def evaluate(board):
    for row in board:
        if row.count('X') == 3:
            return -1
        elif row.count('O') == 3:
            return 1

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == 'X':
            return -1
        elif board[0][col] == board[1][col] == board[2][col] == 'O':
            return 1

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'X':
        return -1
    elif board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'O':
        return 1

 
    return 0

def available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                moves.append((i, j))
    return moves

def get_best_move(board):
    return available_moves(board)[0]

def play_game():
    board = [
        ['_' for _ in range(3)] for _ in range(3)
    ]
    current_player = 'X'

    while True:
        print_board(board)

        if current_player == 'X':
            try:
                x, y = map(int, input("Enter your move (row [0-2] column [0-2]): ").split())
                if 0 <= x <= 2 and 0 <= y <= 2:
                    if board[x][y] == '_':
                        board[x][y] = 'X'
                        current_player = 'O'
                    else:
                        print("Invalid move. That position is already taken. Try again.")
                else:
                    print("Invalid move. Row and column must be between 0 and 2. Try again.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by space.")
        else:
            move = get_best_move(board)
            board[move[0]][move[1]] = 'O'
            current_player = 'X'

        result = evaluate(board)
        if result == 1:
            print_board(board)
            print("AI wins!")
            break
        elif result == -1:
            print_board(board)
            print("Human wins!")
            break
        elif result == 0 and len(available_moves(board)) == 0:
            print_board(board)
            print("It's a draw!")
            break

play_game()
