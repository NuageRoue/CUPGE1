#code 1

def generer_grille_vide(nb_col: int, nb_lig: int) -> list:
    """
        fonction qui genere une grille de jeu du puissance 4 sous la forme d'un tableau de tableau
        on a donc nb_lig tableaux de nb_col elements
    """
    #2 conditions qui verifient que nos valeurs d'entree sont valides
    if type(nb_col) != int or type(nb_lig) != int:
        raise TypeError('nb_col and nb_ligne must be integers')
    if nb_col <= 0 or nb_lig <= 0:
        raise ValueError('nb_col and nb_lig must be positive values')
    return [[0 for i in range(nb_lig)] for j in range(nb_col)] #on renvoie bien un tableau de nb_lig tableaux de len = nb_col



#code 2

def sep_lig(nb_lig: int) -> str:
    """
        fonction qui renvoie la ligne de separation horizontale pour l'affichage de la grille, 
        composee de '+' et de '-'
    """
    lig = '+'
    lig += '-+' * nb_lig
    return lig


def gen_lig(lig: list) -> str:
    """
        fonction qui genere une ligne de la grille
    """
    dico_char = {0: ' ', 1: 'X', 2: 'O'}
    char_lig = '|'
    for col in lig:
        if col not in dico_char:
            raise ValueError('erreur de caractere')
        char_lig += dico_char[col] + '|'
    return char_lig


def end_line(value: int) -> str:
    """
        fonction qui genere la derniere ligne du tableau
    """
    line = ''
    tab = [f' {val}' for val in range(value)]
    for elt in tab:
        line += elt
    return line


def affiche_grille(grille: list) -> None:
    """
        fonction qui affiche la grille complete dans le terminal

        on lui passe en entree la grille sous forme d'une matrice (tableau de tableau), et elle l'affiche,
        avec des separateurs verticaux '|' et horizontaux '+-+'
    """
    sep_hor = sep_lig(len(grille[0]))
    for lig in grille[::-1]:
        print(sep_hor)
        print(gen_lig(lig))
    print(sep_hor)
    print(end_line(len(grille[0])))



#code 3

def peut_jouer(grille: list, colonne: int) -> bool: 
    """
        fonction renvoyant True si la colonne precisee en entree est incomplete dans la grille en entree (si on peut y jouer), sinon False 
    """
    if colonne < len(grille[-1]):
        return (grille[-1][colonne] == 0)
    return False #dans le cas ou le numero de colonne est superieur a la longueur de la liste, on a forcement un coup non valide



#code 4

def joue(grille, colonne, joueur):
    """
        fonction qui modifie le tableau grille dans la colonne en entree, placant le numero du joueur
    """
    i = len(grille) - 1
    while i > 0 and grille[i-1][colonne] == 0:
        print(i)
        i -= 1
    grille[i][colonne] = joueur
    


#code 5

def a_gagne_vert(grille, joueur):
    """
        fonction qui verifie verticalement la victoire du joueur passe en entree
    """
    nb_lig = len(grille)
    nb_col = len(grille[-1])
    for i in range(nb_col):
        for j in range(nb_lig):
            if grille[j][i] == joueur: #si on tombe sur un pion du joueur;
                looked = j
                align = 0
                while looked < nb_lig and grille[looked][i] == joueur: #on verifie verticalement les elements suivants tant qu'ils correspondent
                    align += 1
                    looked += 1
                if align == 4: #quand ils ne correspondent plus, on verifie si on en a bien parcouru 4
                    return True #si c'est le cas, c'est gagne !
    return False


def a_gagne_hor(grille, joueur):
    """
        fonction qui verifie horizontalement la victoire du joueur passe en entree
    """
    nb_lig = len(grille)
    nb_col = len(grille[-1])
    for i in range(nb_lig):
        for j in range(nb_col):
                if grille[i][j] == joueur: #meme principe que la fonction du dessus, mais horizontalement
                    looked = j
                    align = 0
                    while looked < nb_col and grille[i][looked] == joueur :
                        align += 1
                        looked += 1
                    if align == 4:
                        return True
    return False


def a_gagne_diag1(grille, joueur):
    """
        fonction qui verifie sur la diagonale montante la victoire du joueur passe en entree
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
                if align == 4:
                    return True
    return False


def a_gagne_diag2(grille, joueur):
    """
        fonction qui verifie sur la diagonale descendante la victoire du joueur passe en entree
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
                if align == 4:
                    return True
    return False


def a_gagne(grille, joueur):
    """
        fonction qui verifie la victoire du joueur dans toutes les directions 
    """
    return ((a_gagne_vert(grille, joueur) or a_gagne_hor(grille, joueur)) or (a_gagne_diag1(grille, joueur) or a_gagne_diag2(grille, joueur)))



#code 6

def grille_pleine(grille):
    """
        fonction verifiant si la grille passee en argument est remplie ou non :
        si elle est pleine, alors la derniere ligne est remplie, c'est pourquoi on ne verifie que celle-ci

    """
    for elt in grille[-1]:
        if elt == 0:
            return False
    return True



#code 7

def boucle_principale(nb_col, nb_lig):
    
    grille = generer_grille_vide(nb_col, nb_lig)
    joueur_courant = 1

    while not grille_pleine(grille):
        affiche_grille(grille)
        coup = int(input(f"quel est ton prochain coup, joueur {joueur_courant} ? "))
        while not peut_jouer(grille, coup):
            print("erreur ! le coup n'est pas valide \n")
            affiche_grille(grille)
            coup = int(input("\nprière de redonner un coup valide :\n"))
        joue(grille, coup, joueur_courant)
        if a_gagne(grille, joueur_courant):
            affiche_grille(grille)
            print(f"tu as gagné joueur {joueur_courant} ! Félicitations !")
            return True
        joueur_courant = (joueur_courant % 2) + 1 #si joueur courant = 1, alors on a 1 + 1 = 2 ; si joueur courant courant = 2, alors 0 + 1 = 1
    print("ex aequo ! il n'y a pas de gagnant cette fois-ci...")
    return False


if __name__ == "__main__":

    print("test d'affichage \n")
    grid_test1 =   [[1,1,2,1,2,1,1],
                    [2,1,2,2,1,2,2],
                    [0,2,1,1,0,1,2],
                    [0,1,2,2,0,0,0],
                    [0,1,2,1,0,0,0],
                    [0,0,0,0,0,0,0]]
    affiche_grille(grid_test1)
    
    grid_test2 =   [[1,1,2,1,2,1],
                    [2,1,2,2,1,2],
                    [0,2,1,1,0,1],
                    [0,1,2,2,0,0],
                    [0,1,2,1,0,0],
                    [0,1,2,1,0,0],
                    [0,1,2,1,0,0],
                    [0,0,0,0,0,0]]
    affiche_grille(grid_test2)

    print("\n\ntest de 'victoire'")

    grid_testhor1 = [[1,1,1,1,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0]]

    affiche_grille(grid_testhor1)
    print(a_gagne(grid_testhor1, 1))
    
    
    grid_testhor2 = [[0,0,0,0,0,0,0],
                     [0,0,2,2,2,2,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0]]

    affiche_grille(grid_testhor2)
    print(a_gagne(grid_testhor2, 2))

    grid_testhor3 = [[0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,1,1,1,1]]

    affiche_grille(grid_testhor3)
    print(a_gagne(grid_testhor3, 1))

    grid_testhor4 = [[0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,1,1,1,0]]

    affiche_grille(grid_testhor4)
    print(a_gagne(grid_testhor4, 1))

    grid_testvert1 = [[1,0,0,0,0,0,0],
                      [1,0,0,0,0,0,0],
                      [1,0,0,0,0,0,0],
                      [1,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0]]
    
    affiche_grille(grid_testvert1)
    print(a_gagne(grid_testvert1, 1))

    grid_testvert2 = [[0,0,0,0,0,0,0],
                      [0,2,0,0,0,0,0],
                      [0,2,0,0,0,0,0],
                      [0,2,0,0,0,0,0],
                      [0,2,0,0,0,0,0],
                      [0,0,0,0,0,0,0]]

    affiche_grille(grid_testvert2)
    print(a_gagne(grid_testvert2, 2))

    grid_testvert3 = [[0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,2],
                      [0,0,0,0,0,0,2],
                      [0,0,0,0,0,0,2],
                      [0,0,0,0,0,0,2]]

    affiche_grille(grid_testvert3)
    print(a_gagne(grid_testvert3, 2))

    grid_testvert4 = [[0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,1],
                      [0,0,0,0,0,0,1],
                      [0,0,0,0,0,0,1]]

    affiche_grille(grid_testvert4)
    print(a_gagne(grid_testvert4, 1))


    grid_testdiag1 = [[0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0],
                      [0,0,0,0,1,0,0],
                      [0,0,0,0,0,1,0],
                      [0,0,0,0,0,0,1]]

    affiche_grille(grid_testdiag1)
    print(a_gagne(grid_testdiag1, 1))

    grid_testdiag2 = [[0,0,0,1,0,0,0],
                      [0,0,1,0,0,0,0],
                      [0,1,0,0,0,0,0],
                      [1,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0]]

    affiche_grille(grid_testdiag2)
    print(a_gagne(grid_testdiag2, 1))

    filled_grid = [[1,2,1,2,2,1,1],
                     [1,2,1,2,2,1,1],
                     [1,2,1,2,2,1,1],
                     [1,2,1,2,2,1,1],
                     [1,2,1,2,2,1,1],
                     [1,2,1,2,2,1,1]]
    
    affiche_grille(filled_grid)
    print(grille_pleine(filled_grid))

    print("\n\n\n\n test du jeu \n\n")
    boucle_principale(7,6)
    
