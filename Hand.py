class Hand:
  def __init__(self):
    self.cards=[]
    self.value=0
    self.aces=0

  def add_Card(self,card):
      self.cards.append(card)
      self.value += card.rank
      if card.rank == 1:
        self.aces += 1
     
  pass

  def adjust_for_ace(self):
    while self.value >21 and self.aces:
      self.value -=10;
      self.aces -=1;
    pass

