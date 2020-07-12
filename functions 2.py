import playing_cards
def display_hand(hand):
  for card in hand:
         if card[1]=='H':
            print(card[0],'of Heart')
         elif card[1]=='D':
            print(card[0],'of Diamonds',)
         elif card[1] == 'S':
            print(card[0], 'of Spades')
         elif card [1] == 'C':
            print(card[0],'of Clubs')
  return hand

def get_hand_total(hand):
    points = 0
    for card in hand:
      if '1' in card or '2'in card or'3'in card or '4'in card or '5'in card or'6'in card or'7'in card or'8'in card or '9'in card:
       points = points + int(card[0])
      elif 'T' in card or 'J'in card or 'Q'in card or 'K'in card:
       points = points + 10
      elif 'A' in card and points + 10 < 21:
       points = points + 11
      elif 'A' in card and points + 10 > 21:
       points = points + 1
    return points

def get_hit_choice():
    hit_choice = input("Please enter h or s (h = Hit, s = Stand):")
    points =get_hand_total(player_hand)
    while hit_choice != 'h' and hit_choice != 's':
        hit_choice = input("Please enter h or s (h = Hit, s = Stand):")
    if hit_choice == 'h':
        card = playing_cards.deal_one_card()
        player_hand.append(card)
    if hit_choice == 's' and points >= 15:
       player_hand == player_hand
       points =get_hand_total(player_hand)
       print ("player's hand is",points)
       display_hand(player_hand)

    elif hit_choice == 's' and points < 15:
       print('Cannot stand on values less than 15!')
       card = playing_cards.deal_one_card()
       player_hand.append(card)
    return hit_choice



def play_player_hand(player_hand):
    points = get_hand_total(player_hand)
    if points == 21:
       print('*** Blackjack! Player wins! ***')
    else:
       while 15 < points < 21:
         get_hit_choice()
         get_hand_total(player_hand)
         points = get_hand_total(player_hand)
         print('player hand is',points)
         display_hand(player_hand)
       if points > 21:
          print('player busts')
    get_hand_total(player_hand)
    points = get_hand_total(player_hand)
    print("player's hand is",points)
    return player_hand


def play_dealer_hand(dealer_hand):
    card = playing_cards.deal_one_card()
    points = get_hand_total(dealer_hand)
    while points < 17:
        card = playing_cards.deal_one_card()
        dealer_hand.append(card)
        points = get_hand_total(dealer_hand)
        print("Dealer's hand is", points)
        display_hand(dealer_hand)
    if points > 21:
        print('Dealer busts!')
    return dealer_hand





player_hand=[]
dealer_hand =[]
points = 0
play_choice = input('would you like to play blackjack? :')
while play_choice != 'y':
   play_choice = input('would you like to play blackjack? :')
if play_choice == 'y':

    # deal first card
    card = playing_cards.deal_one_card()
    # append one card to dealer_hand list
    dealer_hand.append(card)
    # append it to the player_hand list
    card = playing_cards.deal_one_card()
    player_hand.append(card)

    # deal second card
    card = playing_cards.deal_one_card()

    # append it to the player_hand_list
    player_hand.append(card)

    # total dealer's hand and display
    points = get_hand_total(dealer_hand)
    print("dealer's hand'is", points)
    display_hand(dealer_hand)

    # total player's hand and display
    points = get_hand_total(player_hand)
    display_hand(player_hand)
    play_player_hand(player_hand)
    play_dealer_hand(dealer_hand)
    display_hand(dealer_hand)












