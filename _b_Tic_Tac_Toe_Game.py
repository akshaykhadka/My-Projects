import random
import os
import time


class Player():
    def __init__(self, player):
        self.mark = None
        self.name = player


def display_board(board):
    print("     |     |     ")
    print("  "+board[7]+"  "+"|"+"  "+board[8]+"  "+"|"+"  "+board[9])
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  "+board[4]+"  "+"|"+"  "+board[5]+"  "+"|"+"  "+board[6])
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  "+board[1]+"  "+"|"+"  "+board[2]+"  "+"|"+"  "+board[3])
    print("     |     |     ")

def win_combinations(board, player):

    if ((board[3] == player.mark and board[2] == player.mark and board[1] == player.mark) or
        (board[4] == player.mark and board[5] == player.mark and board[6] == player.mark) or
        (board[7] == player.mark and board[8] == player.mark and board[9] == player.mark) or
        (board[7] == player.mark and board[5] == player.mark and board[3] == player.mark) or
        (board[9] == player.mark and board[5] == player.mark and board[1] == player.mark) or
        (board[1] == player.mark and board[4] == player.mark and board[7] == player.mark) or
        (board[2] == player.mark and board[5] == player.mark and board[8] == player.mark) or
        (board[3] == player.mark and board[6] == player.mark and board[9] == player.mark)):
        print("\n")
        print(player.name + " Wins !!")
        return True
    else:
        return False


def take_mark(board, player):
    position = 100
    while position < 1 or position > 9:
        try:
            position = int(input(player.name + " Choose your position: "))
            if board[position] != " ":
                print("\nThis position's already taken !")
                position = 100
                continue
            else:
                board[position] = player.mark
        except:
            continue


def choose_mark(player1, player2):
    mark = input("\n" + player1.name + ", choose your mark X/O: ")
    if mark[0].upper() == "X":
        print("\n" + player1.name + "'s mark -> 'X'")
        print(player2.name + "'s mark -> 'O'")
        return 'X', 'O'
    else:
        print("\n" + player1.name + "'s mark -> 'X'")
        print(player2.name + "'s mark -> 'O'")
        return 'O', 'X'


# Now starts the game compilation
##################################

# Initializing the game
while True:

    # Printing the welcome note
    print("\nWelcome to the Tic Tac Toe !!")

    # Creating the object player
    player_1 = Player('Player 1')
    player_2 = Player('Player 2')

    # Asking for the mark
    player_1.mark, player_2.mark = choose_mark(player_1, player_2)

    # Initializing the board
    game_board = [" "]*10

    game_on = True

    # Displaying the board for the first 
    print("\n")
    display_board(game_board)

    while game_on:

        # Checking if the game is tied
        if " " not in game_board[1:]:
            print("\nThe Game is Tied !")
            break
        else:
            pass

        # Player 1's turn
        print("\n")
        take_mark(game_board, player_1)
        display_board(game_board)

        # Check for the winning possibilities
        if win_combinations(game_board, player_1):
            break

        # Checking if the game is tied
        if " " not in game_board[1:]:
            print("\nThe Game is Tied !")
            break
        else:
            pass

        # Player 2's turn
        print("\n")
        take_mark(game_board, player_2)
        display_board(game_board)

        # Check again for winning possibilities
        if win_combinations(game_board, player_2):
            break

        # Keep asking until one of the player wins
        
    replay = input("\nDo you want another game? Enter y/n ")
    if replay[0].lower() == 'y':
        continue
    else:
        print("\nThank you for playing !")
        break
