import basic_methods, user_input_actions, game_rules, ui, get_input

deck_count = get_input.get_number("Enter the amount of decks you want:")
deck = basic_methods.return_cards(deck_count)
deck = basic_methods.shuffle_deck(deck)
house_hand = []
player_hand = []
money = get_input.get_number("Enter the desired starting money:")
print("Game starting...\n")

while money > 0:
    deck = basic_methods.reshuffle(deck, deck_count)#shuffle deck when half cards are left
    basic_methods.clear_hands(house_hand, player_hand)#clear hands after each round
    basic_methods.distribute_cards(house_hand, player_hand, deck)
    bet = get_input.get_bet(money)
    money -= bet

    ui.print_ui(house_hand, player_hand, money)
    insurance_bet = get_input.return_insurance_bet(house_hand, player_hand, money)
    money -= insurance_bet
    even_bet = get_input.return_even_bet(player_hand, house_hand, money)
    if insurance_bet or even_bet:#print table again to make it look better
        ui.reprint_ui(house_hand, player_hand, money)
    round_result = str
    while True:#loop where round happens
        action_pick = get_input.get_action_input(house_hand, player_hand, money)
        if action_pick == 's' or action_pick == 'S':
            round_result = user_input_actions.stand(player_hand, house_hand, deck)
            break
        elif action_pick == 'h' or action_pick == 'H':
            round_result = user_input_actions.regular_hit(player_hand, house_hand, deck)
        elif action_pick == 'd' or action_pick == 'D':
            if money < bet:#if not enough money, reprint and return to the loop
                print("Not enough money to double down")
                ui.reprint_ui(house_hand, player_hand, money)
                continue
            else:
                money -= bet
                bet += bet
                round_result = user_input_actions.regular_hit(player_hand, house_hand, deck)
        elif action_pick == 'x' or action_pick == 'X':
            round_result = user_input_actions.surrender()
            break

        if game_rules.check_bust(player_hand):#if player goes bust, break
            break
        else:
            ui.print_ui(house_hand, player_hand, money)

    money += game_rules.payout(bet, round_result)#return money lost or won from that round

    if insurance_bet:#if insurance bet is some number other than 0
        insurance_winning_result = user_input_actions.insurance(house_hand)
        insurance_winning = game_rules.payout(insurance_bet, insurance_winning_result)
        money += insurance_winning
        if insurance_winning:#if bet has been won, print the won amount
            ui.print_ui(house_hand, player_hand, money, round_result, insurance_winning)
        else:#if money has been lost, print the lost amount
            ui.print_ui(house_hand, player_hand, money, round_result, insurance_bet*-1)
    elif even_bet:#if even_bet is some other number than 0
        even_result = user_input_actions.even_money(player_hand, house_hand)
        even_winning = game_rules.payout(even_bet, even_result)
        money += even_winning
        if even_winning:#if money has been won, print the won amount
            ui.print_ui(house_hand, player_hand, money, round_result, even_money = even_winning)
        else:#print the lost amount
            ui.print_ui(house_hand, player_hand, money, round_result, even_money = even_bet*-1)
    else:
        ui.print_ui(house_hand, player_hand, money, round_result)