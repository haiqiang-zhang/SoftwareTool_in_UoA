#
# playing_cards module - PSP Assignment 2, sp2, 2020.
# DO NOT MODIFY!
#

import random


# Deck of cards - first letter represents the face value and
# second letter represents the suit
deck = ['AH','2H','3H','4H','5H','6H','7H','8H','9H','TH','JH','QH','KH',
        'AD','2D','3D','4D','5D','6D','7D','8D','9D','TD','JD','QD','KD',
        'AS','2S','3S','4S','5S','6S','7S','8S','9S','TS','JS','QS','KS',
        'AC','2C','3C','4C','5C','6C','7C','8C','9C','TC','JC','QC','KC']

# Playing deck in use
playing_deck = []


# Function to determine whether there are any cards left in the
# deck of playing cards
# Parameters: No parameters
# Returns: True if the deck is empty, False otherwise
def is_empty_deck():

    # Check to see whether playing deck is empty
    return len(playing_deck) == 0


# Function to rebuild and shuffle the deck
# Parameters: No parameters
# Returns: Nothing is returned from the function.
def reset_deck():
    global playing_deck

    # Create new playing deck
    playing_deck = deck.copy()
    
    # Shuffle deck
    random.shuffle(playing_deck)


# Function to deal one card
# Parameters: No parameters
# Returns: A string (containing two characters) representing
# the card delt, i.e. '2H' meaning 2 of Hearts
def deal_one_card():
    
    # Check to see whether there are any cards left
    if is_empty_deck():
    
        # Rebuild and shuffle deck
        reset_deck()

    # Return a card (string of two characters)
    return playing_deck.pop(0)




