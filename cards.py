import random
from create import *
class Cards(Create_cards):
    create = Create_cards()
    pack_of_cards = create.create_a_deck()

    def __init__(self):
        self.deck = Cards.pack_of_cards[:]
        random.shuffle(self.deck)
    #print(deck)    
    
    def Deal_out(self):
        self.card = self.deck.pop()
        return self.card

    def Hit(self):
        self.card = self.deck.pop()
        return self.card

    def Stay(self):
        None

if __name__ == "__main__":
    Cards()    






 

