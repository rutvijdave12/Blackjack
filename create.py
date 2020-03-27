class Create_cards:
    def create_a_deck(self):
        deck = []
        for suit in ['Hearts','Spades','Clubs','Diamonds']:
            for value in range(1,11):
                if value == 1:
                    deck.append(('Ace'+ ' of '+ suit,(1,11)))
                else:    
                    deck.append((str(value) + ' of ' + suit,value))
            for face in ['Joker','Queen','King']:
                    deck.append((face + ' of ' + suit,10))   
        return deck 
           

   

if __name__ == "__main__":
    create = Create_cards()
    print(create.create_a_deck())