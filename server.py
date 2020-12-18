import socketserver
from config import COMMANDS
from player import Player
from tic_tac_toe import TicTacToe

PLAYER_ONE_SYMBOL = "X"
PLAYER_TWO_SYMBOL = "O"

def getPlayer(playerPos, players):
  idx = playerPos % 2
  return players[idx]

class MyTCPHandler(socketserver.BaseRequestHandler):
  players = []
  playerPos = 0
  playerCount = 0
  
  def handle(self):
    self.data = self.request.recv(1024).strip().decode()
    if cmd == COMMANDS['createPlayer']:
      player = None
      if MyTCPHandler.playerCount == 0:
        MyTCPHandler.playerCount += 1
        player = Player(PLAYER_ONE_SYMBOL, MyTCPHandler.playerCount)
        MyTCPHandler.players.append(player)
        res = "BEGIN{}#{}END".format(COMMANDS['createPlayerAck'], player.id)
        self.request.sendto(bytes(res, 'utf-8'), self.client_address)
      elif MyTCPHandler.playerCount == 1:
        MyTCPHandler.playerCount += 1
        player = Player(PLAYER_TWO_SYMBOL, MyTCPHandler.playerCount)
        MyTCPHandler.players.append(player)
        res = "BEGIN{}#{}END".format(COMMANDS['createPlayerAck'], player.id)
        self.request.sendto(bytes(res, 'utf-8'), self.client_address)
        startGame = "BEGIN{}#{}END".format(COMMANDS['makeMove'], getPlayer(MyTCPHandler.playerPos, MyTCPHandler.players))
        self.request.sendall(bytes(startGame, 'utf-8'))
      else:
        print("INVALID input")
    else:
      print(cmd)

if __name__ == "__main__":
  HOST, PORT = "localhost", 9999
  server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
  server.serve_forever()
