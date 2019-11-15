from Deck import Deck 
from Chips import Chips
from Hand import Hand

class Blackjack:

    cardPosition=0
    def __init__(self):
      self.cardPosition=0
      self.playerChip = Chips()
      self.dealerChip = Chips()
      self.dealerHand = Hand()
      self.playerHand = Hand()




      d=Deck()
      print("Before Shuffle")
      d.printCards()
      d.shuffle()
      print("After Shuffle *****************")
      d.printCards()
    
    def assignCard(self,hand):
        for n in range(0,2):
          typeOfCard = Deck.deck[self.cardPosition];
          hand.card.append(Deck.deck[self.cardPosition])
          if typeOfCard.rank == 1:
            hand.aces = hand.aces + 1
          elif typeOfCard.rank > 10:
             hand.total =  hand.total + 10
          else:
            hand.total =  hand.total + typeOfCard.rank
          self.cardPosition +=1
    pass

    def show_some(self,playerHand,dealerHand):
        for v in dealerHand.card:
          print(v)

        print(dealerHand.total)
        print(dealerHand.aces)
    pass
        
    def show_all(self,playerHand,dealerHand):
          for v in playerHand.card:
            print(v)

          print(playerHand.total)
          print(playerHand.aces)
    pass


    def deal(self):
        self.assignCard(self.dealerHand)
        self.assignCard(self.playerHand)
        print("###############################")
        self.show_some(self.playerHand,self.dealerHand)
        self.show_all(self.playerHand,self.dealerHand)

        self.take_bet(self.dealerChip)
        self.take_bet(self.playerHand)

        while True:
          ans = input("Would you like to hit ")
          if ans=='Yes':
            if not self.player_busts():
              self.hit(self.playerHand)
              continue
        else:
          while True:
            ans = input("Would you like to hit ")
            if ans=='Yes':
              if not self.dealer_busts():
                self.hit(self.dealerHand)
                if self.dealer_wins():
                  print('Dealer win')
                continue
              else:
                print("Dealer Brust")
                break

    pass

    def take_bet(self,chip):
      amount = int(input('Please enter the bet amount -> '))
      if chip.total > amount:
        chip.bet = amount
        chip.total = chip.total - amount
      else:
        print("You Don't have more chip for bet")
    pass
      
    def hit(self,hand):
          typeOfCard = Deck.deck[self.cardPosition];
          hand.card.append(Deck.deck[self.cardPosition])
          if typeOfCard.rank == 1:
            hand.aces = hand.aces + 1
          elif typeOfCard.rank > 10:
             hand.total =  hand.total + 10
          else:
            hand.total =  hand.total + typeOfCard.rank

          self.cardPosition +=1
    pass
      
    def player_busts(self):
     # if playerHand.aces >1 and (21-playerHand.total) >11:
      if self.playerHand.total < 21:
        return False
      return True
    pass
      

    def player_wins(self):
      if self.playerHand.playerHand > 17:
        return True
      return False
    pass

    def dealer_busts(self):
      if self.dealerHand.total <= 17:
        return False
      return True
    pass
          
    def dealer_wins(self):
      if self.dealerHand.total == 17:
        return True
      return False
    pass
          
    def push():
          pass

pass

black = Blackjack()
black.deal()