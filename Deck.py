from Card import Card
import random


class Deck:
  deck  = []
  def __init__(self):
    for s in range(0,4):
      for r in range(1,14):
        self.deck.append(Card(r,s))

  def shuffle(self):
    random.shuffle(self.deck)
  pass

  def deal(self):
    single_Card = self.deck.pop()
    return single_Card

  def printCards(self):
    for v in self.deck :
      print(v)
