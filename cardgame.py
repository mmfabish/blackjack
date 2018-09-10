from random import shuffle, randint

# module instances that store ranks and suits
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card():
    '''
    Abstraction of a playing card.
    '''
    def __init__(self, rank, suit):

        # verify that a valid rank value was provided
        if rank in ranks:
            self.rank = rank
        else:
            raise Exception(f'Invalid rank value: {rank}')

        # verify that a valid suit value was provided
        if suit in suits:
            self.suit = suit
        else:
            raise Exception(f'Invalid suit value: {suit}')

    def __str__(self):
        '''
        Return a string representation of the card.
        '''
        return f'{self.rank} of {self.suit}'

class Deck():
    ''' 
    Abstraction of a deck of cards.
    '''
    def __init__(self):
        # create a list containing all possible cards
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def __str__(self):
        '''
        Display the contents of the deck.
        '''
        return "\n".join(map(str, self.cards))

    def __len__(self):
        '''
        Return the number of cards left in the deck.
        '''
        return len(self.cards)

    def __getitem__(self, index):
        '''
        Allow random-access to the deck of cards.
        '''
        return self.cards[index]

    def deal(self):
        '''
        Returns a card from the deck.
        '''
        # make sure there are cards left to deal
        if len(self) > 0:
            return self.cards.pop()
        else:
            raise Exception("Deck is empty!")

    def deal_random(self):
        '''
        Returns a random card from the deck.
        '''
        return self.cards.pop(randint(0, len(self)))

    def shuffle(self):
        '''
        Shuffle the cards in the deck.
        '''
        shuffle(self.cards)

class Hand():
    '''
    Abstraction of a hand of cards.
    '''
    def __init__(self):
        self.cards = []
        
    def __str__(self):
        '''
        Print the cards in the hand.
        '''
        return "\n".join(self.cards)

    def add(self, card):
        '''
        Add a card to the hand.
        '''
        self.cards.append(card)

    def clear(self):
        '''
        Remove all cards from the hand.
        '''
        self.cards.clear()
        
if __name__ == '__main__':
    deck = Deck()
    print(deck)

    # shuffle the deck
    deck.shuffle()
    print(deck)

    # pull a random card from the deck
    card = deck.deal_random()
    print(f"Your card is {card}")

    # deal the cards
    while(True):
        # try to deal from an empty deck
        try:
            card = deck.deal()
        except Exception as err:
            print("The deck is empty!")
            break
        else:
            print(card)
            continue