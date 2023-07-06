
## creation de la grille : specifique au serveur

def GridMaker(width):
    """
        fonction qui genere une grille de jeu pour le Morpion, de taille minimale 5*5 (pour permettre le jeu)
    """
    return [[0 for i in range(width)] for j in range(width)] # on genere la grille avec une list comprehension


# affichage de la grille : specifique aux clients

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
        print(f"i={i}")
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





#verification de la possibilite de jouer : specifique au serveur

def peut_jouer(grid):
    """
        fonction verifiant si un joueur peut jouer
    """
    for line in grid: # on parcourt chaque ligne
        for col in line :
            if col == 0: # des qu'on tombe sur un 0 (soit une case non utilisee)
                return True #c'est qu'il est possible de jouer : on renvoie True
    return False # si on a tout parcouru sans renvoyer True, on renvoie False




#verification de la victoire d'un joueur : specifique au serveur

def a_gagne_vert(grille: list, joueur: int) -> bool:
    """
        fonction qui verifie verticalement la victoire du joueur passe en entree, renvoyant True si il existe une combinaison verticale du numero du joueur dans le tableau
    """
    nb_lig = len(grille)
    nb_col = len(grille[-1])
    
    for j in range(nb_col):
        for i in range(nb_lig):
            if grille[i][j] == joueur :
                looked = i
                align = 0
                while looked < nb_lig and grille[looked][j] == joueur:
                    align += 1
                    looked += 1
                if align == 5: #quand ils ne correspondent plus, on verifie si on en a bien parcouru 4
                        return True #si c'est le cas, c'est gagne !
    return False

def a_gagne_hor(grille: list, joueur: int) -> bool:
    """
        fonction qui verifie horizontalement la victoire du joueur passe en entree, renvoyant True si il existe une combinaison horizontale du numero du joueur dans le tableau
    """
    nb_lig = len(grille)
    nb_col = len(grille[-1])
    
    for i in range(nb_lig):
        for j in range(nb_col):
            if grille[i][j] == joueur :
                looked = j
                align = 0
                while looked < nb_lig and grille[looked][j] == joueur:
                    align += 1
                    looked += 1
                if align == 5: #quand ils ne correspondent plus, on verifie si on en a bien parcouru 4
                        return True #si c'est le cas, c'est gagne !
    return False


def a_gagne_diag1(grille: list, joueur: int) -> bool:
    """
        fonction qui verifie sur la diagonale montante la victoire du joueur passe en entree, renvoyant True si il existe une combinaison sur la diagonale du numero du joueur dans le tableau
    """
    nb_col = len(grille[-1])
    nb_lig = len(grille)
    for i in range(nb_lig):
        for j in range(nb_col):
            if grille[i][j] == joueur: #meme principe, mais selon la diagonale montante
                looked_lig = i
                looked_col = j
                align = 0
                while (looked_lig < nb_lig and looked_col < nb_col) and grille[looked_lig][looked_col] == joueur:
                    align+=1
                    looked_lig += 1
                    looked_col += 1
                if align == 5:
                    return True
    return False


def a_gagne_diag2(grille: list, joueur: int) -> bool:
    """
        fonction qui verifie sur la diagonale descendante la victoire du joueur passe en entree, renvoyant True si il existe une combinaison sur la diagonale du numero du joueur dans le tableau
    """
    nb_col = len(grille[-1])
    nb_lig = len(grille)
    for i in range(nb_lig):
        for j in range(nb_col):
            if grille[i][j] == joueur: #meme principe, on verifie selon la diagonale descendante
                looked_lig = i
                looked_col = j
                align = 0
                while (looked_lig >= 0 and looked_col < nb_col) and grille[looked_lig][looked_col] == joueur:
                    align+=1
                    looked_lig -= 1
                    looked_col += 1
                if align == 5:
                    return True
    return False


def a_gagne(grille: list, joueur: int) -> bool:
    """
        fonction qui verifie la victoire du joueur dans toutes les directions, renvoyant True si il existe une combinaison du numero du joueur dans le tableau
    """
    return ((a_gagne_vert(grille, joueur) or a_gagne_hor(grille, joueur)) or (a_gagne_diag1(grille, joueur) or a_gagne_diag2(grille, joueur)))


#verification coup valide : specifique aux clients

def coupValide(grid,i,j):
    """
        fonction verifiant si un coup est valide
    """
    nb_col = len(grid[-1])
    nb_lig = len(grid)
    if i < nb_lig and j < nb_col:
        if grid[i][j] == 0:
            return True
    return False