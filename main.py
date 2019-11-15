from Deck import Deck 

class Blackjack:

    dealerCards=[]
    playerCards=[]
    cardPosition=0
    def __init__(self):
      self.dealerCards=[]
      self.playerCards=[]
      self.cardPosition=0
      d=Deck()
    
    def assignCard(self,player):
        for n in range(0,2):
          #print(self.cardPosition)
          #print(Deck.deck[self.cardPosition])
          player.append(Deck.deck[self.cardPosition])
          self.cardPosition +=1
    pass

    def show_some(self,player,dealer):
        for v in player:
          print(v)
    pass
        
    def show_all(self,player,dealer):
          for v in dealer:
            print(v)
    pass


    def deal(self):
        self.assignCard(self.dealerCards)
        self.assignCard(self.playerCards)
        self.show_some(self.playerCards,self.dealerCards)
        self.show_all(self.playerCards,self.dealerCards)
    pass




    def take_bet(self):
        pass
      
    def hit(self,deck,hand):
        pass
      
    def player_busts():
          pass

    def player_wins():
          pass

    def dealer_busts():
          pass
          
    def dealer_wins():
          pass
          
    def push():
          pass

pass

black = Blackjack()
black.deal()