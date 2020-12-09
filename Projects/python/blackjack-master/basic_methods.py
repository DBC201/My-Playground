import random

if __name__ == "__main__":
    print("Error: \"{}\" is not supposed to run as \"__main__\"".format(__file__))
else:
    def return_cards(quantity):#returns deck
        return ( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A']*4 ) * quantity

    def shuffle_deck(input_deck):#shuffles inputted deck
        random.shuffle(input_deck)
        return input_deck

    def draw_card(side, input_deck):#draws card from inputted size to inputted deck
        if len(input_deck) == 0:#if no cards in input deck, no cards are drawn
            return 0
        else:
            side.append(input_deck.pop(len(input_deck)-1))
            return input_deck

    def calculate_hand_value(side):#returns the value of hand
        value = 0
        aces = []
        for c in range(0,len(side)):#adds up the card values beside aces
            if side[c] == 'A':
                aces.append(c)#stores aces in a list
                continue
            elif isinstance(side[c], str):
                value += 10
            else:
                value += side[c]
        for x in range(0,len(aces)):
            if (value + len(aces)-1 + 11) <= 21:#decides if each ace should be taken as 1 or 11
                value += 11
                aces.pop(x)
            else:
                value += 1
        return value

    def reshuffle(input_deck, quantity):#shuffles the deck while printing out a message
        if len(input_deck) <= len(return_cards(quantity)) / 2:#reshuffle when half deck
            print("Shuffling deck")
            input_deck = return_cards(quantity)
            input_deck = shuffle_deck(input_deck)
        return input_deck

    def clear_hands(house, player):#clears hands
        house.clear()
        player.clear()

    def distribute_cards(house, player, input_deck):#distributes cards
        for x in range(2):
            draw_card(house, input_deck)
            draw_card(player, input_deck)