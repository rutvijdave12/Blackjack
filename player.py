class Player:
    coins = 1000
    card_list = []
    def __init__(self,name):
        self.name = name
        self.balance = Player.coins
        print(self.name + " your balance is: " +str(self.balance))

    def Place_a_bet(self):
        while True:
            
            try:
                self.bet = int(input(self.name + " please place your bet: "))
                if self.bet > self.balance:
                    raise Exception(self.name + ",the bet you've placed exceeds your balance which is " +str(self.balance)+ ".")
                else:
                    print(self.name+ " you have bet " +str(self.bet)+ " coins.")  

            except ValueError :
                print(self.name+ " Please place a valid bet ")
                continue

            except Exception as msg:
                print(msg)
                continue          
            
            else:
                self.balance -= self.bet
                print(self.name + " your balance is: " +str(self.balance)+ ".")
                break
    
    def Display_cards(self):
        print(self.name+ " your card(s) is/are: ",end="" )
        for i in Player.card_list:
            #print(Player.card_list)
            print(i,end=" ")

    def Player_cards(self,card):

        Player.card_list.append(card)
        
        #self.Display_cards()
        

    


    def reset(self):
        del Player.card_list[:] 
        


    def result(self,blackjack_in_two = False):
        if not blackjack_in_two:
            winning = 2*self.bet
            self.balance += winning
        elif blackjack_in_two == "PUSH":
            winning = self.bet
            self.balance +=winning
        else:
            winning = 3*self.bet
            self.balance += winning
        print(self.name+ " You've won " +str(winning)+ " coins.")
        
if __name__ == "__main__":
    player1 = Player('Rutvij')
    player1.Place_a_bet()
    player1.Player_cards()

     