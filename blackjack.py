import cardgame

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10}

class Hand:
    '''
    Abstraction of a hand of blackjack.
    '''
    def __init__(self):
        self.cards = []
        self._score = 0
        self.aces = 0

    def __getitem__(self, index):
        return self.cards[index]

    def add_card(self, card):
        '''
        Add a card to the hand.
        '''
        self.cards.append(card)

        # Ace values can be 1 or 11, don't add them directly to the score tally
        if card.rank == 'Ace':
            self.aces += 1
        else:
            self._score += values[card.rank]

    def is_blackjack(self):
        '''
        Determine if the current hand is a blackjack.
        '''
        return self.score() == 21

    def is_bust(self):
        '''
        Determine if the current hand's value is greater than 21.
        '''
        return self.score() > 21

    def score(self):
        '''
        Return the current hand value.
        '''
        # an ace will be worth 11 points if the player's score is less than or equal to 10
        if self._score <= 10 and self.aces > 0:
            return self._score + 11 + (self.aces - 1)
        else:
            return self._score + self.aces

    def __str__(self):
        '''
        Print the cards in the hand.
        '''
        return "\n".join(map(str, self.cards))

class Player:
    '''
    Abstraction of a player in a game of blackjack.
    '''
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def __str__(self):
        '''
        Return a string representation of the player.
        '''
        return self.name

    def deal_card(self, card):
        '''
        Add a new card to the player's hand.
        '''
        self.hand.add_card(card)

    def print_hand(self):
        '''
        Print the contents of the current hand of cards.
        '''
        print("{}'s current hand: ".format(self.name))
        for card in self.hand:
            print("\t* {}".format(card))

class Game():
    '''
    Abstraction of a game of blackjack.
    '''
    def __init__(self):
        self.deck = cardgame.Deck()
    
    def play(self):
        '''
        Play a single game of blackjack.
        '''
        # shuffle the deck
        self.deck.shuffle()
        
        # create two new players (one human, one computer)
        player = Player('Matt')
        dealer = Player('Dealer')

        # deal the dealer and player two cards each
        for _ in range(2):
            player.deal_card(self.deck.deal())
            dealer.deal_card(self.deck.deal())

        takeTurn = True
        while takeTurn:
            # display the player's current cards
            player.print_hand()
            print("Your current score = {}".format(player.hand.score()))

            # determine if the player hit blackjack
            if player.hand.is_blackjack():
                print("Blackjack!  You win!")
                takeTurn = False
            elif player.hand.is_bust():
                print("Sorry, you busted!")
                takeTurn = False
            else:
                # prompt the player for his/her next move
                response = input("Hit or stay? [h/s] ").lower()

                if response == 'h':
                    player.deal_card(self.deck.deal())
                elif response == 's':
                    takeTurn = False
                else:
                    print("Invalid response.  Please enter h for hit or s for stay.")

        # let the dealer take his/her turn
        takeTurn = not (player.hand.is_blackjack() or player.hand.is_bust())
        while takeTurn:
            # display the dealer's current cards
            dealer.print_hand()
            print("Dealer's current score = {}".format(dealer.hand.score()))

            # determine if the dealer hit blackjack
            if dealer.hand.is_blackjack():
                print("Blackjack!  The dealer wins!")
                takeTurn = False
            elif dealer.hand.is_bust():
                print("The dealer busted...you win!")
                takeTurn = False
            elif dealer.hand.score() > player.hand.score():
                print("The dealer wins!")
                takeTurn = False
            else:
                dealer.deal_card(self.deck.deal())
                
if __name__ == '__main__':
    game = Game()
    game.play()