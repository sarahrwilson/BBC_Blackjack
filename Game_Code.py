'''
This code is for a simple game of blackjack, suitable for one player.
Given that blackjack scoring does not depend on suits, I have decided to discount this factor in my deck.
Note that there are some flaws in the reasoning behind the conditions for the value of 'A'. By the conditions,
if a player were to have a hand less than 11 then the 'A' would be set to 11. If the player continuted to play
and then went over 21, the code does not recognise that the 'A' could switch to a value of 1, keeping the player
in the game.
'''

# import packages
import random 

# create a boolean to describe the nature of the player
PlayerIn = True 

# create a list of the deck of cards
Deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
        'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
        'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
        'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

# create an empty lists for the player's cards
Player = []

# define a function of the process of dealing cards to the player
def Deal(Player):
    Card = random.choice(Deck) # choose a random card from the deck
    Player.append(Card)        # add this card to the player's deck
    Deck.remove(Card)          # remove this card from the original deck

# define a function which calculates the total of the player's deck
# note: here it is required to assign values to the ace, jack, queen and king
def Score(Player):
    Score = 0                            # initalize the value of the score at 0
    Royal = ['J', 'Q', 'K']              # create a list of all cards of value 10
    for Card in Player:                  # calculate the score by looping over each possible value for the cards
        if Card in range(1, 11):         # looping over the cards 2 to 10
            Score += Card
        elif Card in Royal:
            Score += 10
        else:                            # condition for the ace
            if Score > 11:               # if score greater than 11 then making A=11 would lose the game so make A=1
                Score += 1
            else:                        # otherwise make A=11
                Score += 11
    return Score

# open the game by dealing the player two cards
for x in range(2):
    Deal(Player)

# create a "while" loop for the game
# note: here the loop gives the player the option to either 'Hit' or 'Stand'
#       it displays the current cards and total at each stage
while PlayerIn:                                                 # open the game with the player active
    print(f"Your hand is {Player} with score {Score(Player)}")  # display initial hand
    if PlayerIn:
        decision = input("Stand or Hit\n")                      # player decides to stand or hit
    if decision == "Stand":                                     # player stands and the player is no longer active
        PlayerIn = False
    else:                                                       # player hits and another card is dealt
        Deal(Player)
    if Score(Player) >= 21:                                     # if player's score is greater than 21, game stops
        break

# create a "for" loop for each senerio of score
if Score(Player) == 21:
    print(f"\nYou have {Player} \nYou win!")                                    # returns "You win!" if the player reaches 21
elif Score(Player) > 21:
    print(f"\nYou have {Player} with score {Score(Player)} \nYou lose!")        # returns "You lose!" once the player is over 21
else:
    print(f"\nYou have {Player} with score {Score(Player)} \nYou were close!")  # returns "You were close!" if the player stand with a hand less than 21
