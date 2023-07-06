
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
    return strGrid + (" " * (NbDigit(len(grid) - 1) + 1)) + ("_" * 2 * len(grid)) # on ajoute aussi la ligne d'underscore : 2 underscore pour chaque caracterem sans oublier les espaces au debut


def MakeGrid(width):
    """
        fonction generant une matrice de taille width * width
    """
    if width < 10:
        width = 10
    return [[0 for i in range(width)]for j in range(width)]

def CanPlay(grid):
    """
        fonction prenant en entree une matrice representant la grille de jeu et :
        - renvoyant True si il est encore possible de jouer (s'il reste un 0 dans la matrice)
        - sinon, False
    """
    for line in grid:
        for elt in line:
            if elt == 0:
                return True
    return False

def MoveIsValid(move):
    """
        fonction recevant un
    """
    if move[0].isupper() and move[1::].isdigit():
        line = int(move[1::])
        col = ord(move[0]) - ord("A")
        if (line < len(grid) and col < len(grid)) and grid[line][col] == 0:
            return True,(line,col)
        return False,None
 


def Play(player, move):
    grid[move[0]][move[1]] = player



#verification de la victoire d'un joueur : specifique au serveur
def WinVert(grid,player):
    lenGrid = len(grid)
    for j in range(lenGrid):
        for i in range(lenGrid):
            if grid[i][j] == player:
                looked = i
                align = 0
                while looked < lenGrid and grid[looked][j] == player:
                    align += 1
                    looked += 1
                if align == 5: #quand ils ne correspondent plus, on verifie si on en a bien parcouru 4
                        return True #si c'est le cas, c'est gagne !
    return False

def WinHor(grid,player):
    lenGrid = len(grid)
    for line in grid:
        for i in range(lenGrid):
            if line[i] == player:
                looked = i
                align = 0
                while looked < lenGrid and line[looked] == player:
                    looked += 1
                    align += 1
                if align == 5:
                    return True
    return False

def WinDiag1(grid, player):
    lenGrid = len(grid)
    for i in range(lenGrid):
        for j in range(lenGrid):
            if grid[i][j] == player: #meme principe, mais selon la diagonale montante
                looked_lig = i
                looked_col = j
                align = 0
                while (looked_lig < lenGrid and looked_col < lenGrid) and grid[looked_lig][looked_col] == player:
                    align+=1
                    looked_lig += 1
                    looked_col += 1
                if align == 5:
                    return True
    return False

def WinDiag2(grid, player):
    """
        fonction qui verifie sur la diagonale descendante la victoire du joueur passe en entree, renvoyant True si il existe une combinaison sur la diagonale du numero du joueur dans le tableau
    """
    lenGrid = len(grid)
    for i in range(lenGrid):
        for j in range(lenGrid):
            if grid[i][j] == player: #meme principe, on verifie selon la diagonale descendante
                looked_lig = i
                looked_col = j
                align = 0
                while (looked_lig >= 0 and looked_col < lenGrid) and grid[looked_lig][looked_col] == player:
                    align+=1
                    looked_lig -= 1
                    looked_col += 1
                if align == 5:
                    return True
    return False

def Win(grid, player):
    return ((WinVert(grid, player) or WinHor(grid, player)) or (WinDiag1(grid, player) or WinDiag2(grid, player)))


playerList = [1,2]
current = 0
grid = MakeGrid(15)
print(GridShow(grid))
print(f"joueur {playerList[current]}, quel est votre coup ?")
while True:
    move = input("Donnez un coup : \n")
    if MoveIsValid(move)[0]:
        Play(playerList[current],MoveIsValid(move)[1])
        if Win(grid, playerList[current]):
            print(f"{playerList[current]} a gagne !")
            break
        current = (current + 1) % 2
        print(GridShow(grid))
        print(f"joueur {playerList[current]}, quel est votre coup ?")
    else:
        print("coup invalide !")

vertTest = [[0,0,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0]]
horTest = [[1,1,1,1,1],[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0]]
