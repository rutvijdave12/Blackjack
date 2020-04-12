class Create_cards:
    deck = []
    def create_a_deck(self):
        #deck = []
        for suit in ['Hearts','Spades','Clubs','Diamonds']:
            for value in range(1,11):
                if value == 1:
                    Create_cards.deck.append(('Ace'+ ' of '+ suit,(1,11)))
                else:    
                    Create_cards.deck.append((str(value) + ' of ' + suit,value))
            for face in ['Joker','Queen','King']:
                    Create_cards.deck.append((face + ' of ' + suit,10))   
        return Create_cards.deck 
           

   

if __name__ == "__main__":
    create = Create_cards()
    print(create.create_a_deck())