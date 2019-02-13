import random

suits = ['♥️Hearts', '♦️Diamonds', '♣️Spades', '♠️Clubs']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10,
          'Ace': 11}


# CLASS

# for card names
class Card():

    def __init__(self, ranks, suits):
        self.rank = ranks
        self.suit = suits
        if self.rank == '10':
            self.short_name = self.rank + self.suit[0]
        else:
            self.short_name = self.rank[0] + self.suit[0]
            self.full_name = self.rank, ' of ', self.suit

    def __str__(self):
        return self.short_name


# To create cards and some method for cards
class Deck():

    def __init__(self, ranks, suits):
        self.deck = []

        for rank in ranks:
            for suit in suits:
                self.deck.append(Card(rank, suit))

    def __str__(self):
        str_card = ''
        for words in self.deck:
            str_card += ' ' + words.__str__()
        return 'we have: ' + str_card

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self, total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# Functions
def take_bet(chip):
    while True:
        try:
            chip.bet = int(input(f'you have {player_chips.total}chips, how much do you want to bet'))

        except:
            print('Please enter number')

        else:
            if chip.bet > chip.total:
                continue
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        hs = input('\nDo you want to hit or stand? ')
        if hs[0].upper() == 'H':
            hit(deck, hand)
            print('\nYou drawed {}'.format(player.cards[-1]))
        elif hs[0].lower() == 's':
            print("\nPlayer stands, its dealer's turn")
            playing = False

        else:
            print('Hit or Stand?')
            continue
        break


def show_some(player, dealer):
    print('\n-----------------------------')
    print("Dealer's cards are: ")
    print("** ,", dealer.cards[1])
    print("Player has: ")
    print(*player.cards, sep=',')
    print(f'Player total point is {player.value}')
    print('-----------------------------')


def show_all(player, dealer):
    print('\n-----------------------------')
    print("Dealer's cards are: ")
    print(*dealer.cards, sep=',')
    print(f'Player total point is {dealer.value}')
    print("Player has: ")
    print(*player.cards, sep=',')
    print(f'Player total point is {player.value}')
    print('-----------------------------')


def player_busts(chips):
    print('\nPlayer bust, dealer win')
    chips.lose_bet()


def player_wins(chips):
    print('\nPlayer win!')
    chips.win_bet()


def dealer_busts(chips):
    print('\nDealer bust, player win')
    chips.win_bet()


def dealer_wins(chips):
    print('\nDealer win!')
    chips.lose_bet()


def push():
    print('\nYou are even, play again')


# game begin
player_chips = Chips(1000)

while True:
    print('-----------------------------')
    print('welcome to play BlackJack')
    print('-----------------------------')
    playing = True
    card = Card(ranks, suits)
    deck = Deck(ranks, suits)
    deck.shuffle()
    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

    take_bet(player_chips)

    show_some(player, dealer)

    while playing:
        hit_or_stand(deck, player)

        show_some(player, dealer)

        if player.value > 21:
            player_busts(player_chips)
            break
        else:
            continue

    if player.value <= 21:
        while dealer.value < 17:
            hit(deck, dealer)
            print('\nDealer drawed one card', dealer.cards[-1])

        show_all(player, dealer)

        if dealer.value > 21:
            dealer_busts(player_chips)

        elif dealer.value < player.value:
            player_wins(player_chips)

        elif dealer.value > player.value:
            dealer_wins(player_chips)

        elif len(player.cards) == 5:
            player_wins(player_chips)

        else:
            push()

    if player_chips.total > 0:
        print('You have {} chips left'.format(player_chips.total))
        play_again = input('Do you want to play another round?')
        if play_again[0].lower() == 'y':
            continue
        else:
            break
    else:
        print("You've lost all your chips, goodbye")
        break















