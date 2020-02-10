import random

def generate_deck(suits=4, type_cards=13):
    """
    Generate a randomized deck of cards

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
    random.shuffle(cards)
    return cards

def play_war(deck):
    a_cards = deck[:int(len(deck)/2)]
    b_cards = deck[int(len(deck)/2):]
    a_stash = []
    b_stash = []
    print("\na_cards: %s, a_stash: %s, \nb_cards: %s, b_stash: %s" % (a_cards, a_stash, b_cards, b_stash))
    round = 1
    while a_cards and b_cards:
        # by using pop, we're playing from the end forward
        a_card = a_cards.pop()
        b_card = b_cards.pop()

        if a_card[list(a_card.keys())[0]] == b_card[list(b_card.keys())[0]]:
            if len(a_cards) > 0 and len(b_cards) > 0:
                a_stash.extend([a_card]+[a_cards.pop()])
                b_stash.extend([b_card]+[b_cards.pop()])
                print("\n-----------------IT'S A WAR!!!!!!!-----------------")
                print("\na_cards: %s, a_stash: %s, \nb_cards: %s, b_stash: %s" % (a_cards, a_stash, b_cards, b_stash))
                continue
            else:
                continue
        elif a_card[list(a_card.keys())[0]] > b_card[list(b_card.keys())[0]]:
            # ordering of a_stash and b_stash is undefined by game rules
            a_cards = [a_card, b_card] + a_stash + b_stash + a_cards
            a_stash = []
            b_stash = []
        elif b_card[list(b_card.keys())[0]] > a_card[list(a_card.keys())[0]]:
            # ordering of a_stash and b_stash is undefined by game rules
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
        print("Both the set of cards are empty!")

if __name__ == "__main__":
    deck = generate_deck()
    play_war(deck)