def game():
    current_player = 'X'
    while True:
        print_board()
        move = input("Player {}, enter your move (1-9): ".format(current_player))
        if board[int(move) - 1] == ' ':
            board[int(move) - 1] = current_player
            result = check_win()
            if result:
                print_board()
                if result == 'Tie':
                    print("It's a tie!")
                else:
                    print("Player {} wins!".format(result))
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move, try again.")

game()
