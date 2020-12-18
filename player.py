class Player():
  id = 1001

  def __init__(self, symbol, pos):
    self.id = Player.id
    self.pos = pos
    self.symbol = symbol

    Player.id += 1

  def __str__(self):
    return "Player {} turn".format(self.pos)