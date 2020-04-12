from player import *
from results import *
from cards import *
from computer import *

def prompt():         
    command = input("Type yes if you want to play again, no to exit: ")
    command = command.upper()
    return command

def Play():
    name = input("Please enter your name: ")
    player1 = Player(name)
    cards1 = Cards()
    comp = Computer()

    while True:
        if len(cards1.deck) < 20:
            # print(len(Cards.deck))
            # print(len(cards1.deck))
            print("Deck Exhausted...")
            print("Creating a new deck of cards...")
            print("Shuffling Cards...")
            cards1 = Cards()
            # print(len(Cards.deck))
            # print(len(cards1.deck))

        result = Results()
        print(player1.name+ " your balance is: "+str(player1.balance))
        player1.Place_a_bet()
        blackjack_in_two = False

        # print(Cards.deck)
        # print()
        # print(cards1.deck) 


        for i in range(2):
            player1.Player_cards(cards1.Deal_out())
            #print()
            comp.Comp_cards(cards1.Deal_out())
        player1.Display_cards()
        print()
        print(str(Computer.card_list[0][0])+ " is one of the cards of the dealer")

        player1_card_lst = result.Decipher(player1.card_list)
        player1_final_value = result.total_check(sum(player1_card_lst),player1_card_lst)

        if player1_final_value == 21:
            print("BLACKJACK")
            print(player1.name+ ", congratulations you've won!")
            blackjack_in_two = True
            player1.result()

        while not blackjack_in_two:
            while True:
                status = ''
                ask = input(player1.name+ " do you want to hit or stay(type accordingly):")
                ask = ask.upper()
                if ask == "HIT":
                    player1.Player_cards(cards1.Hit())
                    player1.Display_cards()
                    print()
                    player1_card_lst = result.Decipher(player1.card_list)
                    player1_final_value = result.total_check(sum(player1_card_lst),player1_card_lst)
                    if player1_final_value == 21:
                        status = "BLACKJACK"
                        print(status)
                        break

                    if player1_final_value < 21:
                        continue
                    else:
                        status = "BUSTED"
                        print(player1.name+ " You're " +status)
                        break
                elif ask == "STAY":
                    cards1.Stay()
                    player1.Display_cards()
                    print()
                    break
                else:
                    print(player1.name+ " you have entered an invalid command.\nPlease try again.")
            if status == "BUSTED":
                break
            elif status == "BLACKJACK":
                print(player1.name + " You've won!")  
                player1.result()
                break

            while True:
                comp.Display_comp_cards()
                print()
                
                comp_card_lst = result.Decipher(Computer.card_list)
                comp_final_value = result.total_check(sum(comp_card_lst),comp_card_lst)
                t = comp.check(comp_final_value)
                if  t == "HIT":
                    comp.Comp_cards(cards1.Hit())

                elif t == "STAY":
                    cards1.Stay()
                    break
                elif t == "BUST":
                    status = "BUSTED"
                    print("Computer " +status)
                    print("Congratulations You won!")
                    break

            if status == "BUSTED":
                print(player1.name + " You've won!")  
                player1.result()
                break
            else:
                final = result.final_result(comp_final_value,player1_final_value)
                if final == "PUSH":
                    player1.result(final)
                elif final:
                    print(player1.name + " You won!")  
                    player1.result()
                break
                
        while True:
            if player1.balance == 0:
                print(player1.name+ " you don't have enough coins to play!")
                command = "NO"
                break
            else:
                command = prompt() 
            if command in ["YES","NO"]:
                break
            else:
                continue      
        # command = input("Type yes if you want to play again, no to exit: ")
        # command = command.upper()
        if command == "YES":
            player1.reset()
            comp.reset()
            print("\n"*20) 

            continue
        elif command == "NO":
            break

    print(player1.name+ " Thank You for playing!") 
             



Play()  

    