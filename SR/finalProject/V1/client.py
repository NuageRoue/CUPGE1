import socket as soc

IP = "127.0.0.1"
PORT = 5050


socket_client = soc.socket(soc.AF_INET, soc.SOCK_DGRAM)

#affichage de la grille :
def NbDigit(nb):
    """
        fonction retournant le nombre de chiffre composant un nombre
    """
    i = 1
    while (nb//10): # tant que la partie entiere de la division du nombre par 10 n'est pas nulle :
        nb //= 10 # on retire le premier chiffre a droite en effectuant cette division ;
        i += 1 # on incremente notre compteur de chiffre.
    return i

def Line(nb, gridLine, nbMax=10):
    """
        fonction qui specifiquement genere une ligne de la grille
        on specifie un numero de taille maximale afin de parfaire l'affichage (si on a comme taille maximale un nombre a 2 chiffres, on ajoutera un espace a ceux n'ayant qu'un chiffre)
    """
    charList = [".", "X", "O"]
    line = (NbDigit(nbMax) - NbDigit(nb)) * " " + f"{nb}|" # on commence par ajouter notre chiffre au debut de la ligne, avec suffisamment d'espace " " pour ne pas causer de decalage plus tard : on en ajoute autant qu'il manque de chiffre a notre nombre pour arriver au nombre maximal
    for i in gridLine:
        line += (" " + charList[i])
    return line+"\n"

def GridShow(grid):
    """
        fonction du client affichant une grille dans le terminal
    """
    strGrid = ""
    for i in range(len(grid)):
        strGrid += Line(i, grid[i], len(grid)) # on ajoute toutes les lignes a la grille
    print(strGrid + (" " * (NbDigit(len(grid) - 1) + 1)) + ("_" * 2 * len(grid))) # on ajoute aussi la ligne d'underscore : 2 underscore pour chaque caracterem sans oublier les espaces au debut





#reception/envoi
def ToGrid(data):
    """
        fonction convertissant la grille transformée (et SEULEMENT la grille) en liste classique
    """
    line = data[0]
    grid = [[0 for i in range(line)] for j in range(line)]
    data = data[1::]
    for elt in range(len(data)):
        grid[elt//line][elt%line] = data[elt]
    return grid
def ToByteArray1(grid):    
    """
        fonction convertissant la grille en message demandant au joueur de jouer
    """
    arrayToReturn = bytearray([1, len(grid)])
    for line in grid:
        arrayToReturn += bytearray(line)
    return arrayToReturn










#jeu en lui-meme
def chooseUsername():
    username = input("nom d'utilisateur : ")
    message = bytearray([0])
    message += username.encode()
    socket_client.sendto(message,(IP,PORT))
    return username

def EndGame(code):
    if code == 0:
        print(f"personne ne remporte la partie !")
        print("le jeu est terminé ! (Appuyez sur Ctrl+C pour quitter)")
    elif code == playerCode:
        print(f"{playerName} remporte la partie !")
        print("le jeu est terminé ! (Appuyez sur Ctrl+C pour quitter)")
    else:
        print(f"{otherPlayer} remporte la partie !")
        print("le jeu est terminé ! (Appuyez sur Ctrl+C pour quitter)")

def joue(grid,playerCode):
    print("Entrez votre prochain coup :\n")
    while True:
        coup = input()
        if coup[0].isupper() and coup[1::].isdigit():
            line = int(coup[1::])
            col = ord(coup[0]) - ord("A")
            if (line < len(grid) and col < len(grid)) and grid[line][col] == 0:
                print(line,col)
                grid[line][col] = playerCode
                GridShow(grid)
                return ToByteArray1(grid)
        print("Coup Invalide !")
        pass

def traiteMessage(data,playerCode,otherPlayer):
    if data[0] == 0:
        playerCode = data[1]
        otherPlayer = data[2::].decode()
    elif data[0] == 1:
        grid = ToGrid(data[1::])
        GridShow(grid)
        data = joue(grid, playerCode)
        socket_client.sendto(data,(IP,PORT))
    elif data[0] == 2:
        code = data[1]
        grid = ToGrid(data[2::])
        GridShow(grid)
        EndGame(code)
    return playerCode,otherPlayer


playerName = chooseUsername()
playerCode = 0
otherPlayer = ""

while True:
    

    data,addr = socket_client.recvfrom(65536)
    playerCode,otherPlayer = traiteMessage(data,playerCode,otherPlayer)

#playerCode = 1
#grid = [[0 for i in range(15)] for j in range(15)]
#data = ToByteArray1(grid)
#print(ToGrid(data[1::]))
#grid = ToGrid(data[1::])
#GridShow(grid)
#joue(grid)