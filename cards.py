import random
from create import *
class Cards(Create_cards):
    create = Create_cards()
    deck = create.create_a_deck()

    random.shuffle(deck)
    #print(deck)    
    
    def Deal_out(self):
        self.card = Cards.deck.pop()
        return self.card

    def Hit(self):
        self.card = Cards.deck.pop()
        return self.card

    def Stay(self):
        None

if __name__ == "__main__":
    Cards()    






 

