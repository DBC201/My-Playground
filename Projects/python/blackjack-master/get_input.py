import game_rules, ui

if __name__ == "__main__":
    print("Error: \"{}\" is not supposed to run as \"__main__\"".format(__file__))
else:
    #get money and deck count
    def get_number(prompt):
        while True:
            number = input(prompt)
            if not number.isdigit():
                print("Enter a valid integer!")
                continue
            else:
                return int(number)

    def get_bet(money, bet_type = "regular"):
        print()
        while True:  # check for input error for bet
            if bet_type == "regular":
                inp_bet = input("Enter your bet:")
            else:
                inp_bet = input("Enter {} bet:".format(bet_type))

            if not inp_bet.isdigit():
                print("Enter a valid number input!")
                continue
            bet = int(inp_bet)
            if bet > money:
                print("You don't have that much money, you have {:d} dollars.".format(money))
                continue
            break
        return bet

    def return_insurance_bet(house, player, money):
        if game_rules.ace_showing(house) and not game_rules.check_blackjack(player):
            while True:
                insurance_pick = input("Would you like insurance(y/n):")
                if insurance_pick.lower() == 'y':
                    return get_bet(money, "insurance")
                elif insurance_pick.lower() == 'n':
                    break
                else:
                    print("Wrong input")
        return 0

    def get_action_input(house, player, money):
        while True:
            pick = input()
            if pick.lower() != 's' and pick.lower() != 'h' and pick.lower() != 'd' and pick.lower() != 'x':
                print("Wrong input, try again.")
                ui.reprint_ui(house, player, money)
                continue
            else:
                return pick

    def return_even_bet(player, house, money):
        if game_rules.check_blackjack(player) and game_rules.ace_showing(house):#conditions for even bet to be printed
            while True:
                even_pick = input("Would you like even money(y/n):")
                if even_pick.lower() == 'y':
                    return get_bet(money, "even money")
                elif even_pick.lower() == 'n':
                   break
                else:
                    print("Wrong input")
        return 0

