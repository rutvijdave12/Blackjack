class Computer:
    card_list = []
    def Comp_cards(self,card):
        Computer.card_list.append(card)
        #return str(Computer.card_list[0]) + ' is one of the cards of the dealer'

    def Display_comp_cards(self):
        print("Computer's cards are: ",end="" )
        for i in Computer.card_list:
            print(i,end=" ")

    def check(self,comp_card_value):
        if comp_card_value<17:
            return "HIT"
        elif comp_card_value>=17 and comp_card_value<=21:
            return "STAY"
        else:
            return "BUST"

            

    def reset(self):
        del Computer.card_list[:] 

    
           


        
             

