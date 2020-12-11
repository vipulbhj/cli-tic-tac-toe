class TicTacToe():
  def __init__(self, botSymbol):
    self.botSymbol = botSymbol
    self.board = ["#" for _ in range(9)]


  def printBoard(self):
    print("**************BOARD****************")
    for i in range(0, 9):
      if i % 3 == 0:
        print()
      print("  {}  ".format(self.board[i]), end="")
    print("\n")


  def isWon(self, playerSymbol):
    if self.board[0] == self.board[1] and self.board[0] == self.board[2] and self.board[0] == playerSymbol:
      '''
        X X X       O O O
        # # #   OR  # # #  
        # # #       # # #
      '''
      return True
    elif self.board[3] == self.board[4] and self.board[3] == self.board[5] and self.board[3] == playerSymbol:
      '''
        # # #        # # #
        X X X  OR    O O O  
        # # #        # # #
      '''
      return True
    elif self.board[6] == self.board[7] and self.board[6] == self.board[8] and self.board[6] == playerSymbol:
      '''
        # # #          # # #
        # # #   OR     # # #
        X X X          O O O  

      '''
      return True
    elif self.board[0] == self.board[3] and self.board[0] == self.board[6] and self.board[0] == playerSymbol:
      '''
        X # #       O # #
        X # #   OR  O # #  
        X # #       O # #
      '''
      return True
    elif self.board[1] == self.board[4] and self.board[1] == self.board[7] and self.board[1] == playerSymbol:
      '''
        # X #       # O #
        # X #   OR  # O #  
        # X #       # O #
      '''
      return True
    elif self.board[2] == self.board[5] and self.board[2] == self.board[8] and self.board[2] == playerSymbol:
      '''
        # # X       # # O
        # # X   OR  # # O  
        # # X       # # O
      '''
      return True
    elif self.board[0] == self.board[4] and self.board[0] == self.board[8] and self.board[0] == playerSymbol:
      '''
        X # #       O # #
        # X #   OR  # O #  
        # # X       # # O
      '''
      return True
    elif self.board[2] == self.board[4] and self.board[2] == self.board[6] and self.board[2] == playerSymbol:
      '''
        # # X       # # O
        # X #   OR  # O #  
        X # #       O # #
      '''
      return True

    return False

  
  def choosePosition(self):
    while True:
      try:
        userInput = int(input("Enter the position you want to play at: ").strip())
        boardIdx = userInput - 1
        if boardIdx >= 0 and self.board[boardIdx] == "#":
          return boardIdx
        else:
          print('Invalid Input. Please try again')  
      except Exception:
        print('Invalid Input. Please try again')

  
  def playMove(self, position, playerSymbol):
    self.board[position] = playerSymbol

  def isFinished(self):
    return "#" not in self.board

  def botMove(self):
    currentBoardState = [x for x in self.board]
    pos = self.calcBotMove(self.botSymbol)
    self.board = currentBoardState
    self.playMove(pos, self.botSymbol)
    

  def calcBotMove(self, playerSymbol):
    availableBoardIdxs = [idx for idx in range(9) if self.board[idx] == "#"]
    for idx in availableBoardIdxs:
      self.playMove(idx, playerSymbol)
      self.printBoard()
      if playerSymbol == "X" and self.isWon(playerSymbol):
        pass
      elif playerSymbol == "O" and self.isWon(playerSymbol):
        return idx
      elif self.isFinished():
        pass
      else:
        playerSymbol = "X" if playerSymbol == "O" else "O"
        if self.calcBotMove(playerSymbol):
          return idx
        else:
          pass
      self.board[idx] = "#"
    return False