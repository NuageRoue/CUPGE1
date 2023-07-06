import socket as soc
from morpion import *

BALISE_NEW_PLAYER = "__new_player__:"
BALISE_NEW_MOVE = "__move__:"
BALISE_VICTORY = "__victory__:"
BALISE_END = "__end__"
IP = "127.0.0.1"
PORT = 5050
socket_serveur = soc.socket(soc.AF_INET, soc.SOCK_DGRAM)

class Player():
    def __init__(self,pseudo, nb, IP_PORT):
        self.pseudo = pseudo
        self.nb = nb
        self.addr = IP_PORT
    def __str__(self):
        return self.pseudo
    def __repr__(self):
        return self.pseudo
    def sentGridTo(self,serv,grid):
        serv.sendto(ToByteArray(grid),self.addr)

def ToByteArray(grid):
    arrayToReturn = bytearray(len(grid))
    for line in grid:
        arrayToReturn += bytearray(line)
    return arrayToReturn
                                                                              
def ToGrid(data):
    line = data[0]
    grid = [[0 for i in range(line)] for j in range(line)]
    
    data = data[1::]

    for elt in range(len(data)):
        grid[elt//line][elt%line] = data[elt]
    return grid

test = [[0,1,2],[1,2,2],[2,0,1]]
test = ToByteArray(test)
print(ToGrid(test))

def tour(player, grid):
    socket_serveur.sendto(ToByteArray(grid), player.addr)
    addr = None
    while addr != player.addr:
        data, addr = socket_serveur.recvfrom(65536)
    grid = ToGrid(data)



def NewPlayer(data, addr, nbPlayer):
    """
        fonction creant et renvoyant une instance de la classe joueur 
    """
    pseudo = ":".join(data.split(":")[1::])
    return Player(pseudo,nbPlayer,addr)


def MainLoop(width = 15):
    """
        fonction gerant la boucle principale du jeu
    """

    socket_serveur.bind((IP,PORT))
    grid = GridMaker(width)
    playerList = []

    #recuperation des 2 joueurs :
    while len(playerList) != 2:
        data, addr = socket_serveur.recvfrom(65536)
        data = data.decode()
        if data.startswith(BALISE_NEW_PLAYER):
            playerList.append(NewPlayer(data, addr, len(playerList)+1))

    #lancement de la boucle de jeu :
    current = 0
    while True:
        tour(playerList[current], grid)
        for player in playerList:
            player.sentGridTo(socket_serveur,grid)
        if a_gagne(grid, playerList[current]):
            socket_serveur.sendto((BALISE_VICTORY+f"{player}").encode(), player.addr)
