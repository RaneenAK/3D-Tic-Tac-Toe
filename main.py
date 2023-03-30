import random
import time


def get_player_names():
    p1 = input("Give 1st player name:")
    p2 = input("Give 2nd player name:")
    return [p1, p2]


def get_board_visual(boards):
    board_A1 = f"""
                    {"Board 1"}
                        
                 0      1     2            
                     |     |     
            0     {boards[0][0][0]}  |  {boards[0][0][1]}  |  {boards[0][0][2]}  
                _____|_____|_____
                     |     |     
            1     {boards[0][1][0]}  |  {boards[0][1][1]}  |  {boards[0][1][2]}  
                _____|_____|_____
                     |     |     
            2     {boards[0][2][0]}  |  {boards[0][2][1]}  |  {boards[0][2][2]}  
                     |     |     
   
   
   
                    {"Board 2"}

                 0      1     2            
                     |     |     
            0     {boards[1][0][0]}  |  {boards[1][0][1]}  |  {boards[1][0][2]}  
                _____|_____|_____
                     |     |     
            1     {boards[1][1][0]}  |  {boards[1][1][1]}  |  {boards[1][1][2]}  
                _____|_____|_____
                     |     |     
            2     {boards[1][2][0]}  |  {boards[1][2][1]}  |  {boards[1][2][2]}  
                     |     |     
    
    
    
                    {"Board 3"}

                 0      1     2            
                     |     |     
            0     {boards[2][0][0]}  |  {boards[2][0][1]}  |  {boards[2][0][2]}  
                _____|_____|_____
                     |     |     
            1     {boards[2][1][0]}  |  {boards[2][1][1]}  |  {boards[2][1][2]}  
                _____|_____|_____
                     |     |     
            2     {boards[2][2][0]}  |  {boards[2][2][1]}  |  {boards[2][2][2]}  
                     |     |     
        """
    print(board_A1)


#
def first_player_move(player, boards):
    choice = input(f"It`s {player}`s turn, please provide chosen board number and coordinates(ex:1 0 1): ").split()
    if boards[int(choice[0]) - 1][int(choice[1])][int(choice[2])] == " ":
        boards[int(choice[0]) - 1][int(choice[1])][int(choice[2])] = "X"
        return boards
    else:
        print("Cant place your move there, try again")
        time.sleep(1.5)
        return False


#
def second_player_move(player, boards):
    choice = input(f"It`s {player}`s turn, please provide chosen board number and coordinates(ex:1 0 1): ").split()
    if boards[int(choice[0]) - 1][int(choice[1])][int(choice[2])] == " ":
        boards[int(choice[0]) - 1][int(choice[1])][int(choice[2])] = "O"
        return boards
    else:
        print("Cant place your move there, try again")
        time.sleep(1.5)
        return False


def check_diagonal(boards):
    if boards[0][0][0] == boards[1][1][1] == boards[2][2][2]:
        return True
    elif boards[0][0][2] == boards[1][1][1] == boards[2][2][0]:
        return True
    elif boards[0][2][0] == boards[1][1][1] == boards[2][0][2]:
        return True
    elif boards[0][2][2] == boards[1][1][1] == boards[2][0][0]:
        return True


def check_win(boards):
    # 3-D diagonal line
    if boards[0][0][0] == boards[1][1][1] == boards[2][2][2]:
        return True
    elif boards[0][0][2] == boards[1][1][1] == boards[2][2][0]:
        return True
    elif boards[0][2][0] == boards[1][1][1] == boards[2][0][2]:
        return True
    elif boards[0][2][2] == boards[1][1][1] == boards[2][0][0]:
        return True
    # 3-D Rows
    for x in range(3):
        for y in range(3):
            for z in range(3):
                if boards[x][y][z] == boards[x][y][z] == boards[x][y][z]:
                    return True
    # Check each board
    for board in boards:
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return True

        # Check columns
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
                return True

        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
            return True
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
            return True


def print_winner_message(player):
    print(
        "   .----------------. .----------------. .-----------------..-----------------..----------------. .----------------. ")
    print(
        "  | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |")
    print(
        "  | | _____  _____ | | |     _____    | | | ____  _____  | | | ____  _____  | | |  _________   | | |  _______     | |")
    print(
        "  | ||_   _||_   _|| | |    |_   _|   | | ||_   \|_   _| | | ||_   \|_   _| | | | |_   ___  |  | | | |_   __ \    | |")
    print(
        "  | |  | | /\ | |  | | |      | |     | | |  |   \ | |   | | |  |   \ | |   | | |   | |_  \_|  | | |   | |__) |   | |")
    print(
        "  | |  | |/  \| |  | | |      | |     | | |  | |\ \| |   | | |  | |\ \| |   | | |   |  _|  _   | | |   |  __ /    | |")
    print(
        "  | |  |   /\   |  | | |     _| |_    | | | _| |_\   |_  | | | _| |_\   |_  | | |  _| |___/ |  | | |  _| |  \ \_  | |")
    print(
        "  | |  |__/  \__|  | | |    |_____|   | | ||_____|\____| | | ||_____|\____| | | | |_________|  | | | |____| |___| | |")
    print(
        "  | |              | | |              | | |              | | |              | | |              | | |              | |")
    print(
        "  | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |")
    print(
        "   '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' ")
    print(f"Player {player} won! Congratulations!")


if __name__ == '__main__':
    # players = get_player_names()  # Player names assignment
    players = ["moshe", "semion"]
    first_player = random.choice(players)  # Randomly assigning first player
    second_player = players[1] if first_player == players[0] else players[0]  # Assigning second player

    board_A = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    board_B = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    board_C = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    win = False
    moves = 0
    boards = [board_A, board_B, board_C]
    while not win:
        get_board_visual(boards)
        while not first_player_move(first_player, boards):
            pass
        moves += 1
        if moves > 4:
            if check_win(boards):
                print_winner_message(first_player)
                break
        print("--------------------------------------------------------------------------------------")
        get_board_visual(boards)
        while not second_player_move(second_player, boards):
            pass
        moves += 1
        if moves > 4:
            if check_win(boards):
                print_winner_message(second_player)
                break
