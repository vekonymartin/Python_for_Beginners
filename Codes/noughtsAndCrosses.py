# Task 1 - tic-tac-toe

board = ["  ", "1", "2", "3", "1 ", "-", "-", "-", "2 ", "-", "-", "-", "3 ", "-", "-", "-"]
player_1_turn = True
have_winner = False
while not have_winner:
    # Dislpay the board
    for i in range(0, 16, 4):
        print(board[i] + '|' + board[i + 1] + '|' + board[i + 2] + '|' + board[i + 3] + '|')
    if player_1_turn:
        print("Player 1's turn")
    else:
        print("Player 2's turn")
    new_place = False
    while not new_place:
        # Check if the player input is on the board
        row = column = 10
        while row > 3 or row < 1:
            row = int(input("Which row you need?\n"))
        while column > 3 or column < 1:
            column = int(input("Which column you need?\n"))
        if board[4 * row + column] == "-":
            new_place = True
    # Player put the mark on the board
    if player_1_turn:
        board[4 * row + column] = "o"
    else:
        board[4 * row + column] = "x"
    # Check rows
    if board[5] == board[6] and board[5] == board[7] and board[5] != "-":
        if player_1_turn:
            print("Player 1 win.")
        else:
            print("Player 2 win.")
        have_winner = True
    if board[9] == board[10] and board[9] == board[11] and board[9] != "-":
        if player_1_turn:
            print("Player 1 win.")
        else:
            print("Player 2 win.")
        have_winner = True
    if board[13] == board[14] and board[13] == board[15] and board[13] != "-":
        if player_1_turn:
            print("Player 1 win.")
        else:
            print("Player 2 win.")
        have_winner = True
    # Check columns
    if board[5] == board[9] and board[5] == board[13] and board[5] != "-":
        if player_1_turn:
            print("Player 1 win.")
        else:
            print("Player 2 win.")
        have_winner = True
    if board[6] == board[10] and board[6] == board[14] and board[6] != "-":
        if player_1_turn:
            print("Player 1 win.")
        else:
            print("Player 2 win.")
        have_winner = True
    if board[7] == board[11] and board[7] == board[15] and board[7] != "-":
        if player_1_turn:
            print("Player 1 win.")
        else:
            print("Player 2 win.")
        have_winner = True
    # Check diagonals
    if board[5] == board[10] and board[5] == board[15] and board[5] != "-":
        if player_1_turn:
            print("Player 1 win.")
        else:
            print("Player 2 win.")
        have_winner = True
    if board[7] == board[10] and board[7] == board[13] and board[7] != "-":
        if player_1_turn:
            print("Player 1 win.")
        else:
            print("Player 2 win.")
        have_winner = True
    # Tie
    if not have_winner and "-" not in board:
        have_winner = True
        print("It's a tie.")
    if not have_winner:
        if player_1_turn:
            player_1_turn = False  # player2
        else:
            player_1_turn = True  # player1
for i in range(0, 16, 4):
    print(board[i] + '|' + board[i + 1] + '|' + board[i + 2] + '|' + board[i + 3] + '|')
