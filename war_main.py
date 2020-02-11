import random

def generate_deck(suits=4, type_cards=13):
    """
    This method generate a randomized deck of cards

    Parameters:
    suits (int): Number of suits to include in the deck
    type_cards (int): Number of cards in one suit

    Returns:
    It returns a list of cards in a deck. 
    Every card in this list is a dictionary with the card name as the key and card value as the value.
    """
    cards = []
    for suite in range(suits):
        for type_card in range(1, type_cards+1):
            # Setting the key-value pair for every card
            if (type_card == 1):
                cards.append({'A':type_cards+1})
            elif (type_card == 11):
                cards.append({'J': type_card})
            elif (type_card == 12):
                cards.append({'Q': type_card})
            elif (type_card == 13):
                cards.append({'K': type_card})
            else:
                cards.append({type_card:type_card})
    # Randomize the set of cards in the deck
    random.shuffle(cards)
    return cards

def play_war(deck):
    """
    This method simulates the war card game. After every round, it prints the list and count of cards in each player's set,
    the list and count of cards in the stash for both players and at the end of the game, it prints
    the name of the winning player.

    Parameters:
    deck (list): It is a list of dictionaries where each dictionary corresponds to a single card in the deck.
    """
    a_cards = deck[:int(len(deck)/2)]
    b_cards = deck[int(len(deck)/2):]
    a_stash = []
    b_stash = []
    print("\na_cards: %s, a_stash: %s, \nb_cards: %s, b_stash: %s" % (a_cards, a_stash, b_cards, b_stash))
    round = 1
    while a_cards and b_cards:
        # The pop() here means we play with the card that is at the end of the list
        a_card = a_cards.pop()
        b_card = b_cards.pop()

        # This is the case if the drawn cards are of equal value
        if a_card[list(a_card.keys())[0]] == b_card[list(b_card.keys())[0]]:
            if len(a_cards) > 0 and len(b_cards) > 0:
                a_stash.extend([a_card]+[a_cards.pop()])
                b_stash.extend([b_card]+[b_cards.pop()])
                print("\n-----------------IT'S A WAR!!!!!!!-----------------")
                print("\na_cards: %s, a_stash: %s, \nb_cards: %s, b_stash: %s" % (a_cards, a_stash, b_cards, b_stash))
                continue
            else:
                continue
        
        # This is the case when a_card wins over the b_card
        elif a_card[list(a_card.keys())[0]] > b_card[list(b_card.keys())[0]]:
            a_cards = [a_card, b_card] + a_stash + b_stash + a_cards
            a_stash = []
            b_stash = []

        # This is the case when b_card wins over the a_card
        elif b_card[list(b_card.keys())[0]] > a_card[list(a_card.keys())[0]]:
            b_cards = [b_card, a_card] + b_stash + a_stash + b_cards
            a_stash = []
            b_stash = []

        print("\na_cards: %s, a_stash: %s, \nb_cards: %s, b_stash: %s" % (a_cards, a_stash, b_cards, b_stash))

        print("After round %s: \na_cards_count: %s, a_stash_count: %s, b_cards_count: %s, b_stash_count: %s" %
           (round, len(a_cards), len(a_stash), len(b_cards), len(b_stash)))
        round += 1

    if(len(a_cards) > len(b_cards)):
        print("A_cards wins!!!")
    elif(len(b_cards) > len(a_cards)):
        print("B_cards wins!!!")
    else:
        print("Both the set of cards are empty! It's a tie!")

if __name__ == "__main__":
    deck = generate_deck()
    play_war(deck)