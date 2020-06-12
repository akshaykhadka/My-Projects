import random

# Creating 'suits', 'rank' and 'values of card' for the Cards
suits = ('Spades', 'Clubs', 'Hearts', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


# Creating 'class' for Card
class Card:
    # Initializing the Card by giving it a 'suit' and a 'rank'
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # returns a string of the form: eg. 'Spades of Three'
        return self.suit + " of " + self.rank


class Deck:
    def __init__(self):
        self.deck = []
        # Inserting all the Cards in the Deck
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_cards = ""
        for card in self.deck:
            deck_cards += "\n" + str(card)
        return "The Deck has: " + deck_cards

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


# Creating 'class' for the Hand (pack of cards either with the 'Player' or 'Dealer'
# while playing the game)
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def aces_adjuster(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self, total_chips=100):
        self.total_chips = total_chips
        self.chips_for_bet = 0

    # If the Player wins the bet
    def win_bet(self):
        # The chips used for the bet is added to the total chips
        self.total_chips += self.chips_for_bet

    # If the Player loses the bet
    def lose_bet(self):
        # Chips used for the bet is deducted from the total chips
        self.total_chips -= self.chips_for_bet


def take_bet(chips):
    chips.chips_for_bet = float("inf")

    # Keep asking for the bet until it is less than the total chips available
    while chips.chips_for_bet > chips.total_chips:
        try:
            chips.chips_for_bet = int(
                input("\nEnter the amount of chips you want to bet -> "))
        except:
            continue


def hit(deck, hand):
    # Hitting the deck and adjusting for the value of the Ace card
    hand.add_card(deck.deal())
    hand.aces_adjuster()


def hit_or_stand(deck, hand):
    global game_on  # To control an upcoming while loop

    while True:
        x = input("Do you want to hit or stand? Enter h/s: ")

        if x[0].lower() == 'h':
            hit(deck, hand)  # Function defined above
        elif x[0].lower() == 's':
            print("\nPlayer stands. Now Dealer's turn.")
            game_on = False
        else:
            print("Sorry didn't understand your entry.")
            print("Please try again.")
            continue
        break

# Function for showing the partial hand of the dealer


def show_partial(player, dealer):
    print("\nDealer's Hand: ")
    print(" <card hidden> ")
    print(" ", dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep="\n ")


# Function for revealing the complete hand
def show_complete(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep="\n")
    print("Dealer's Hand: ", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n')
    print("Player's Hand: ", player.value)


# Functions for managing the end game scenarios
def player_bust(player_chips):
    print("\nPlayer busts !")
    player_chips.lose_bet()


def player_wins(player_chips):
    print("\nPlayer Wins !")
    player_chips.win_bet()


def dealer_bust(player_chips):
    print("\nDealer busts !")
    player_chips.win_bet()


def dealer_wins(player_chips):
    print("\nDealer Wins !")
    player_chips.lose_bet()


def push():
    print("\nThe game is tied. It's a push !")


def replay():
    pass

# Now starts the game compilation
####################################


game_on = True

while True:

    # Printing the welcome note
    print("\nWelcome to the Black_Jack Game !")

    # Shuffling the deck
    deck = Deck()  # Creating the deck object first
    deck.shuffle()

    # Creating Chips object for the player and the dealer
    player_chips = Chips()
    dealer_chips = Chips()

    # Taking bet from the player
    take_bet(player_chips)

    # Creating the player's hand and dealer's hand
    player_hand = Hand()
    dealer_hand = Hand()

    # Dealer two cards each for the player and the dealer
    hit(deck, player_hand)
    hit(deck, dealer_hand)
    hit(deck, player_hand)
    hit(deck, dealer_hand)

    # Setting game_on = True again for the continuation of the loop
    game_on = True

    # Creating a flag for busting of player
    bust = False

    while game_on:

        # Showing only partial cards
        show_partial(player_hand, dealer_hand)

        # Asking the player either to hit or stand
        hit_or_stand(deck, player_hand)

        # Checking whether the player's bust!
        if player_hand.value > 21:
            bust = True
            break
        else:
            continue

    if bust:
        show_complete(player_hand, dealer_hand)
        player_bust(player_chips)
        print("\nDealer Wins !")
        print("\nYour total chips: {}".format(player_chips.total_chips))
    else:

        # Dealer's turn to hit
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Checking if the dealer got bust
        if dealer_hand.value > 21:
            show_complete(player_hand, dealer_hand)
            print("\nDealer got Bust !")
            player_wins(player_chips)
            print("\nYour total chips: {}".format(player_chips.total_chips))
        else:

            # Checking who won the game
            if dealer_hand.value == player_hand.value:
                show_complete(player_hand, dealer_hand)
                push()
            elif dealer_hand.value > player_hand.value:
                show_complete(player_hand, dealer_hand)
                dealer_wins(player_chips)
                print("\nYour total chips: {}".format(player_chips.total_chips))
            else:
                show_complete(player_hand, dealer_hand)
                player_wins(player_chips)
                print("\nYour total chips: {}".format(player_chips.total_chips))

    # Asking for the replay
    is_replay = input("\nDo you want to play again? Enter y/n: ")

    if is_replay[0].lower() == 'y':
        continue
    else:
        print("\nThank you for playing !")
        break
