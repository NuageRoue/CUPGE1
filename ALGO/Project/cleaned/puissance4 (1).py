import doctest

def generer_grille_vide(nb_col,nb_lig) :
    return []

def affiche_grille(grille) :
    """
    >>> affiche_grille([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],\
        [0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]])
    +-+-+-+-+-+-+-+
    | | | | | | | |
    +-+-+-+-+-+-+-+
    | |X|O|X| | | |
    +-+-+-+-+-+-+-+
    | |X|O|O| | | |
    +-+-+-+-+-+-+-+
    | |O|X|X| |X|O|
    +-+-+-+-+-+-+-+
    |O|X|O|O|X|O|O|
    +-+-+-+-+-+-+-+
    |X|X|O|X|O|X|X|
    +-+-+-+-+-+-+-+
     0 1 2 3 4 5 6
    """
    pass

def peut_jouer(grille,colonne) :
    return False

def joue(grille,colonne,joueur) :
    pass

def a_gagne_vert(grille,joueur) :
    return False

def a_gagne_hor(grille,joueur) :
    return False

def a_gagne_diag1(grille,joueur) :
    return False

def a_gagne_diag2(grille,joueur) :
    return False

def a_gagne(grille,joueur) :
    return False

def grille_pleine(grille) :
    return False

def boucle_principale() :
    pass

if __name__ == "__main__" :
    doctest.testmod()
    boucle_principale()