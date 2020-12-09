import game_rules

if __name__ == "__main__":
    print("Error: \"{}\" is not supposed to run as \"__main__\"".format(__file__))
else:
    #possible actions: hit, stand, surrender, insurance, double down, even_money

    def stand(player_deck, house_deck, input_deck):#makes the player stand and returns round result
        game_rules.house_hit(house_deck, input_deck)
        act_result = game_rules.check_win(house_deck, player_deck)
        return act_result

    def regular_hit(player_deck, house_deck, input_deck):#makes player hit and returns round result
        game_rules.player_hit(player_deck, input_deck)
        game_rules.house_hit(house_deck, input_deck)
        return game_rules.check_win(house_deck, input_deck)

    def surrender():
        return "surrender"

    def insurance(house_deck):
        if game_rules.check_insurance(house_deck):
            return "insurance"
        else:
            return "lose"

    def even_money(player_deck, house_deck):
        if game_rules.check_even_money(player_deck, house_deck):
            return "even"
        else:
            return "lose"
