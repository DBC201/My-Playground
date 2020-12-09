if __name__ == "__main__":
    print("Error: \"{}\" is not supposed to run as \"__main__\"".format(__file__))
else:
    def print_hands(house, player, round = "going"):
        if round == "going":
            print("House: [[], ", end='')
            for c in range(len(house)):
                if len(house) == 1:
                    print(']')
                elif c == 0:
                    continue
                elif c == len(house)-1:
                    print("{}]".format(str(house[c])))
                else:
                    print("{}, ".format(str(house[c])), end='')
        else:
            print("House: {}".format(house))
        print("You: {}".format(player))
        return True

    def print_actions(player_card_number):
        print("type \'s\' for stand")
        print("type \'h\' for hit")
        print("type \'x\' for surrender")
        if player_card_number <= 2:#cards can't be less than 2, but the point is you can only double down once
            print("type \'d\' for double down")

    def print_ui(house_deck, player_deck, input_money, round_status = "going", insurance_money = 0, even_money = 0):
        print_hands(house_deck, player_deck, round_status)
        print()
        if round_status == "going":
            print_actions(len(player_deck))
        else:
            print_even_or_insurance("Insurance", insurance_money)
            print_even_or_insurance("Even money", even_money)
            print("The round ended with a {}".format(round_status))
            print("Money: ${:d}".format(input_money))
        return True

    def reprint_ui(house, player, money):
        print("Printing board again\n")
        print_ui(house, player, money)

    def print_even_or_insurance(type, winning):
        if winning > 0:
            print("{0} payback total(including {0} bet) is {1:d}".format(type, winning))
        elif winning < 0:
            print("You have lost {:d} from {}".format(winning, type))
