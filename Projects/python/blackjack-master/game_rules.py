import basic_methods

if __name__ == "__main__":
    print("Error: \"{}\" is not supposed to run as \"__main__\"".format(__file__))
else:
    #plus initial money included in payout
    payout_coefficient = {#coefficient for the total amount of return depending on result
        "insurance" : 2,
        "blackjack" : 1.5,
        "win" : 1,
        "tie" : 0,
        "even" : 1,
        "lose" : -1,
        "surrender" : -0.5
    }

    def check_blackjack(side):#checks if the inputted side has blackjack
        if len(side) == 2 and basic_methods.calculate_hand_value(side) == 21:
            return True
        else:
            return False

    def check_bust(side):#checks if inputted side is bust
        if basic_methods.calculate_hand_value(side) > 21:
            return True
        else:
            return False

    def house_hit(house, input_deck):#makes house hit if total value < 17 else does nothing
        while basic_methods.calculate_hand_value(house) < 17 and len(input_deck) != 0:
            basic_methods.draw_card(house, input_deck)
        return house

    def player_hit(player, input_deck):#makes player hit(draw a card and removes it from the deck)
        basic_methods.draw_card(player, input_deck)
        return player

    def check_win(house, player):#checks for different winning conditions
        if check_blackjack(house) and check_blackjack(player):
            return "tie"
        elif not check_blackjack(house) and check_blackjack(player):
            return "blackjack"
        elif check_bust(player):
            return "lose"
        elif check_bust(house):
            return "win"
        elif basic_methods.calculate_hand_value(house) == basic_methods.calculate_hand_value(player):
            return "tie"
        elif basic_methods.calculate_hand_value(house) < basic_methods.calculate_hand_value(player):
            return "win"
        elif basic_methods.calculate_hand_value(house) > basic_methods.calculate_hand_value(player):
            return "lose"
        else:
            print("Error at game_rules.check_win(house, player)")
            return False

    def payout(bet, result):#returns payout depending on round result, using the dictionary defined on top
        return int(bet + (bet * payout_coefficient[result]))

    def ace_showing(house):#checks if house has a ace showing, used for insurance
        if len(house) < 2:
            return False
        elif house[1] == 'A':
            return True
        else:
            return False

    def check_insurance(house):#returns true if house has blackjack, if there is insurance bet, this will be useful
       if ace_showing(house) and check_blackjack(house):
           return True
       else:
           return False

    def check_even_money(player, house):#returns true if both sides have blackjack, used for even money bet
        if check_blackjack(player) and check_blackjack(house):
            return True
        else:
            return False
