from tic_tac_toe import TicTacToe

PLAYER_ONE_SYMBOL = "X"
BOT_SYMBOL = "O"

def main():
  try:
    game = TicTacToe(BOT_SYMBOL)
    while True:
      game.printBoard()
      
      # Prompt Player One to play the move.
      print('Player One')
      pos = game.choosePosition()
      game.playMove(pos, PLAYER_ONE_SYMBOL)
      
      game.printBoard()
      
      if game.isWon(PLAYER_ONE_SYMBOL):
        print('Player One - Won the game')
        break
      elif game.isFinished():
        print("It's a draw")
        break
      
      game.botMove()
      game.printBoard()

      if game.isWon(BOT_SYMBOL):
        print('Player Two - Won the game')
        break
      elif game.isFinished():
        print("It's a draw")
        break
  except Exception as e:
    print("Something went wrong.")
    print("Error: ", e)

if __name__=='__main__':
  main()