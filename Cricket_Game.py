import random


def toss_coin():
    coin = input("Choose 'E' for Even and 'O' for odd -> ")
    print(" ")
    your_num = int(input("Now select a number between 0-5: "))
    random_num = random.randint(0, 5)
    print(" ")

    print("your number {} and computer's number {}".format(your_num, random_num))
    random_sum = your_num + random_num
    if coin.lower() == 'e':
        if random_sum % 2 == 0:
            return True
        else:
            return False

    if coin.lower() == 'o':
        if random_sum % 2 == 0:
            return False
        else:
            return True


def zero_adjuster(x, y):
    if x == 0:
        return y
    else:
        return x


def game_replay():
    replay = input("Do you want another game? Enter y/n: ")

    if replay.lower() == 'y':
        return True
    else:
        return False


def win_check(player_score, computer_score):
    if player_score > computer_score:
        print("You Won !!!")
    elif computer_score > player_score:
        print("You Lost :( ")
    else:
        print("The Game is drawn.")


def check_if_won(x, y):
    pass


# Now starts the game compilation...
#####################################

while True:
    # Printing the Welcome Note
    print("Welcome to the Game of Cricket !")
    print(" ")

    # Starting the game
    game_on = False
    play = input("Are you ready to play? Enter y/n: ")

    if play == 'y':
        game_on = True
    else:
        game_on = False
        break

    # Tossing the coin
    player_chance = False
    computer_chance = False

    if toss_coin():
        player_chance = True
        print(" ")
        print("You Won the toss, your batting first...")
    else:
        computer_chance = True
        print(" ")
        print("You Lost the toss, you'll bowl first...")

    player_score = 0
    computer_score = 0

    while game_on:

        # Setting OUT = False first
        out = False

        # Initiating player's turn...
        while not out and player_chance:
            # Asking for the user input and generating computer's number
            user_input = -1
            while not (user_input >= 0 and user_input < 6):
                user_input = int(input("Enter a number between 0-5: "))
            computer_number = random.randint(0, 5)

            # Checking wether OUT or NOT OUT
            if user_input == computer_number:
                out = True
                print("Computer's number: {}".format(computer_number))
                print("\n")
                print("OUT !!!")
                print("\n")
                print("Your total score {}".format(player_score))
                print("\n")
                if computer_chance:
                    game_on = False
                    computer_chance = False
                    break
                computer_chance = True
                break
            else:
                # Adjusting for the zero
                user_input = zero_adjuster(user_input, computer_number)

                player_score += user_input
                print("Computer's number: {}".format(computer_number))
                print("Your score -> {}".format(player_score))
                print(" ")

            # Check whether the player has already won
            if computer_chance:
                if player_score > computer_score:
                    game_on = False
                    computer_chance = False
                    break

            # Keep asking for the player input until the player is OUT

        # Again setting OUT = False for the computer
        out = False

        # Initiating computer's turn...
        while not out and computer_chance:
            # Again asking for the user input and generating computer's number
            user_input = -1
            while not (user_input >= 0 and user_input < 6):
                user_input = int(input("Enter a number between 0-5: "))
            computer_number = random.randint(0, 5)

            # Checking whether the computer is OUT or NOT
            if user_input == computer_number:
                out = True
                print("Computer's number: {}".format(computer_number))
                print("\n")
                print("Computer is OUT !!!")
                print("\n")
                print("computer's total score {}".format(computer_score))
                print("\n")
                if player_chance:
                    game_on = False
                    break
                player_chance = True
                break
            else:
                computer_number = zero_adjuster(computer_number, user_input)
                computer_score += computer_number
                print("Computer's number: {}".format(computer_number))
                print("computer's score -> {}".format(computer_score))
                print(" ")

            # Check wether the computer has already won
            if player_chance:
                if computer_score > player_score:
                    game_on = False
                    break

            # Keep asking for the player's input until the computer is OUT

    # Deciding who won the game
    print("Your total score {}".format(player_score))
    print("computer's total score {}".format(computer_score))
    print(" ")
    win_check(player_score, computer_score)
    print("\n")

    # Asking user for the replay
    if game_replay():
        game_on = True
    else:
        print("\n")
        print("Thank You for playing !!")
        break
