from Deck import Deck 
from Chips import Chips
from Hand import Hand

cardPosition = 0
playing = True

def take_bet(chips):
  while True:
    try:
       chips.bet = int(input('Please Enter the amout for Bet '))
    except ValueError:
      print('Sorry, a bet must be an integer!')
    else:
      if chips.total < chips.bet:
        print("Sorry, your bet can't exceed",chips.total)
      else:
        break;
    pass

def hit(deck,hand):
    hand.add_Card(deck.deal())
    hand.adjust_for_ace()
pass

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
      x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
      if x[0].lower() == 'h':
        hit(deck,hand)
      elif x[0].lower() == 's':
        print("Player stands. Dealer is playing.")
        playing = False
      else:
            print("Sorry, please try again.")
            continue
      break
    pass

def show_some(player,dealer):
  print("\nDealer's Hand:")
  print(" <card hidden>")
  print('',dealer.cards[1])  
  print("\nPlayer's Hand:", *player.cards, sep='\n ')    
pass
    
def show_all(player,dealer):
  print("\nDealer's Hand:", *dealer.cards, sep='\n ')
  print("Dealer's Hand =",dealer.value)
  print("\nPlayer's Hand:", *player.cards, sep='\n ')
  print("Player's Hand =",player.value)
pass

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()
    pass

def player_wins(player,dealer,chips):
    print("Player Winn!")
    chips.win_bet()
    pass

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.lose_bet()
    pass
    
def dealer_wins(player,dealer,chips):
    print("Dealer win!")
    chips.win_bet()
    pass
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")


while True:
  print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\Dealer hits until she reaches 17. Aces count as 1 or 11.')
  deck = Deck()
  deck.shuffle()

  player_hand = Hand()
  player_hand.add_Card(deck.deal())
  player_hand.add_Card(deck.deal())

  dealer_hand = Hand()
  dealer_hand.add_Card(deck.deal())
  dealer_hand.add_Card(deck.deal())

  player_chips = Chips()
  take_bet(player_chips)

  show_some(player_hand,dealer_hand)

  while playing:
    hit_or_stand(deck, player_hand)
    show_some(player_hand,dealer_hand)

    if player_hand.value>21:
     player_busts(player_hand,dealer_hand,player_chips)
     break
    
  if player_hand.value<=21:
    while dealer_hand.value < 17:
      hit(deck,dealer_hand)

    # Show all cards
    show_all(player_hand,dealer_hand)
          # Test different winning scenarios
    if dealer_hand.value > 21:
      dealer_busts(player_hand,dealer_hand,player_chips)
    elif dealer_hand.value > player_hand.value:
      dealer_wins(player_hand,dealer_hand,player_chips)
    elif dealer_hand.value < player_hand.value:
      player_wins(player_hand,dealer_hand,player_chips)
    else:
      push(player_hand,dealer_hand)

  print("\nPlayer's winnings stand at",player_chips.total)

  new_game=input("Would you like to play another hand? Enter 'y' or 'n' ")
  if new_game[0].lower()=='y':
    playing=True
    continue
  else:
    print("Thanks for playing")
    break



    # def __init__(self):
    #   self.cardPosition=0
    #   self.playerChip = Chips()
    #   self.dealerChip = Chips()
    #   self.dealerHand = Hand()
    #   self.playerHand = Hand()

    #   d=Deck()
    #   print("Before Shuffle")
    #   d.printCards()
    #   d.shuffle()
    #   print("After Shuffle *****************")
    #   d.printCards()
    
    # def assignCard(self,hand):
    #     for n in range(0,2):
    #       typeOfCard = Deck.deck[self.cardPosition];
    #       self.cardPosition +=1
    # pass

    # def show_some(self,playerHand,dealerHand):
    #     for v in dealerHand.card:
    #       print(v)

    #     print(dealerHand.total)
    #     print(dealerHand.aces)
    # pass
        
    # def show_all(self,playerHand,dealerHand):
    #       for v in playerHand.card:
    #         print(v)

    #       print(playerHand.total)
    #       print(playerHand.aces)
    # pass


    # def deal(self):
    #     self.assignCard(self.dealerHand)
    #     self.assignCard(self.playerHand)
    #     print("###############################")
    #     self.show_some(self.playerHand,self.dealerHand)
    #     self.show_all(self.playerHand,self.dealerHand)

    #     self.take_bet(self.dealerChip)
    #     self.take_bet(self.playerHand)

    #     while True:
    #       ans = input("Would you like to hit ")
    #       if ans=='Yes':
    #         if not self.player_busts():
    #           self.hit(self.playerHand)
    #           continue
    #     else:
    #       while True:
    #         ans = input("Would you like to hit ")
    #         if ans=='Yes':
    #           if not self.dealer_busts():
    #             self.hit(self.dealerHand)
    #             if self.dealer_wins():
    #               print('Dealer win')
    #             continue
    #           else:
    #             print("Dealer Brust")
    #             break

    # pass

    # def take_bet(self,chips):
    #    while True:
    #     try:
    #         chips.bet = int(input('How many chips would you like to bet? '))
    #     except ValueError:
    #         print('Sorry, a bet must be an integer!')
    #     else:
    #         if chips.bet > chips.total:
    #             print("Sorry, your bet can't exceed",chips.total)
    #         else:
    #             break
    # pass
      
    # def hit(self,hand):
    #    hand.add_card(deck.deal())
    #    hand.adjust_for_ace()


    #       typeOfCard = Deck.deck[self.cardPosition];
    #       hand.card.append(Deck.deck[self.cardPosition])
    #       if typeOfCard.rank == 1:
    #         hand.aces = hand.aces + 1
    #       elif typeOfCard.rank > 10:
    #          hand.total =  hand.total + 10
    #       else:
    #         hand.total =  hand.total + typeOfCard.rank

    #       self.cardPosition +=1
    # pass
      
    # def player_busts(self):
    #  # if playerHand.aces >1 and (21-playerHand.total) >11:
    #   if self.playerHand.total < 21:
    #     return False
    #   return True
    # pass
      

    # def player_wins(self):
    #   if self.playerHand.playerHand > 17:
    #     return True
    #   return False
    # pass

    # def dealer_busts(self):
    #   if self.dealerHand.total <= 17:
    #     return False
    #   return True
    # pass
          
    # def dealer_wins(self):
    #   if self.dealerHand.total == 17:
    #     return True
    #   return False
    # pass
          
    # def push():
    #       pass
