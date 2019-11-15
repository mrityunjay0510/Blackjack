class Card:
  suites = ["Clubs", "Diamonds", "Hearts", "Spades"]
  ranks = [None,'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
  def __init__(self,rank,suit):
    self.rank=rank
    self.suit=suit

  def __str__(self):
    return self.ranks[self.rank] +' of '+ self.suites[self.suit]