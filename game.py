



def gameLoop(players):
  playerPos = 0
  try:
    game = TicTacToe()
    while True:
      game.printBoard()
      player = getPlayer(playerPos, players)
      playerPos += 1
      print(player)
      pos = game.choosePosition()
      game.playMove(pos, player.symbol)
      game.printBoard()
      
      if game.isWon(player.symbol):
        print('{} - Won the game'.format(player))
        break
      elif game.isFinished():
        print("It's a draw")
        break
  except Exception as e:
    print(e)
