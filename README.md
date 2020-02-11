# War Card Game

### Rules for the game:-

1. A deck of randomized 52 cards is distributed between two users equally (26 each).

2. Each player plays a card. Higher card wins. Winner takes both cards and add them to the deck.
   - The last element in the list is always the playing card. The cards that are won are added at the beginning of the list.

3. If the two cards played are of equal value, then there is a "war".
   Both players place the next card of their pile face down and then another card face-up. 
   The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck.
   If the face-up cards are again equal then the battle repeats with another set of face-down/up cards. 
   This repeats until one player's face-up card is higher than their opponent's.
   - In order to simulate this rule in the code, a stash is maintained for both the players
   - When the cards have equal value, each card is placed in their respective stash
   - The next card of each list (face down card) is also added to the respective stash
   - The next card is then the playing card. Winner will take all the cards in both the stashes as well

4. Game is over when a player doesn't have any cards. The player with cards remaining is the winner.

### Assumptions

 1) The game is played by two players
 2) The order of value of the suits is ignored
 3) The deck of 52 cards is actually made up of 13 unique cards repeated 4 times
 4) The Ace which is the dictionary with the key 'A', has the highest value
 5) When a player wins a battle, the cards won are added to the deck (beginning of the list)
    in the following order: the winning card, the losing card, the winning player's stash, the losing player's stash

### Future work
 1) The game can be expanded to include more than 2 players
 2) If there are 3 players, deal out 17 cards each. If there are 4 players, deal out 13 cards each
 3) The suits can be taken into account in the following order of value: Spades > Hearts > Diamonds > Clubs
 4) A major expansion would be to deploy this on a GUI. This interface will just allow the user to
    start the game simulation. The actual card images can be read using OCR, making the GUI even better.


 ### Corner Cases
 1) If the cards are not shuffled randomly, every round will be a war and the game will always end up in a tie!
 2) If the cards are same even after a "war", same procedure of the current and next card to stash, and playing
    with the next card. 
 3) If this time the cards are not of equal value, the winner takes 10 cards. If the cards are of equal value,
    the same procedure is followed as in 2.