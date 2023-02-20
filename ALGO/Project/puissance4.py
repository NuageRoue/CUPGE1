import doctest

#OLIVEIRA Clement

#code 1

def generer_grille_vide(nb_col: int, nb_lig: int) -> list:
    """
        fonction qui genere une grille de jeu du puissance 4 sous la forme d'un tableau de tableau
        on a donc nb_lig tableaux de nb_col elements

        attention, les valeurs d'entree ne peuvent etre inferieure ou egale a 0: si c'est le cas, la fonction renvoie False (pour utiliser la fonction dans la boucle principale)

    exemple:

    >>> generer_grille_vide(7,6)
    [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    
    >>> generer_grille_vide(5,5)
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    
    >>> generer_grille_vide(0,0)
    False
    
    >>> generer_grille_vide(True, 'test')
    False
    """
    #2 conditions qui verifient que nos valeurs d'entree sont valides
    if type(nb_col) != int or type(nb_lig) != int: #si on a bien des ints
        return False
    if nb_col <= 0 or nb_lig <= 0: #si ils sont bien strictement positif
        return False
    return [[0 for i in range(nb_col)] for j in range(nb_lig)] #on renvoie bien un tableau contenant nb_lig tableaux de nb_col entiers



#code 2

def sep_lig(nb_lig: int) -> str:
    """
        fonction qui renvoie la ligne de separation horizontale pour l'affichage de la grille, 
        composee de '+' et de '-'.
        etant donne le programme, cette fonction est appelee avec un argument (càd le nombre de ligne) toujours valide : elle ne gere donc pas les cas d'erreurs (erreur de type, de signe...)

        Cependant, la valeur attendue est un entier strictement positif (en principe superieur a 4)
    exemple:
    >>> sep_lig(5)
    '+-+-+-+-+-+'

    >>> sep_lig(1)
    '+-+'

    >>> sep_lig(0)
    '+'
    """
    lig = '+'
    lig += '-+' * nb_lig
    return lig


def gen_lig(lig: list) -> str:
    """
        fonction qui genere une ligne de la grille : elle prend en entree une des sous-listes de la grille (une ligne du tableau)

    exemple :

    >>> gen_lig([0,0,1,1,2])
    '| | |X|X|O|'

    >>> gen_lig([1,0,1,1,2,0,1,2,1])
    '|X| |X|X|O| |X|O|X|'

    >>> gen_lig([1,0,1,1,2,0,1,2,3])
    Traceback (most recent call last):
    ...
    ValueError: erreur de caractere
    """
    dico_char = {0: ' ', 1: 'X', 2: 'O'}
    char_lig = '|'
    for col in lig:
        if col not in dico_char:
            raise ValueError('erreur de caractere')
        char_lig += dico_char[col] + '|'
    return char_lig


def end_line(nb_col: int) -> str:
    """
        fonction qui genere la derniere ligne du tableau : une succession de chiffres correspondant aux differents indices        
        etant donne le programme, cette fonction ne peut qu'etre appelee par le programme avec des valeurs 
        en entree (càd le nombre de colonne) valides : la fonction ne gere donc pas les cas d'erreurs (erreur de type, de signe...)    
        
        Cependant, la valeur attendue est un entier strictement positif (en principe superieur a 4).

        exemple:
    
    >>> end_line(7)
    ' 0 1 2 3 4 5 6'

    >>> end_line(1)
    ' 0'
    """
    line = ''
    tab = [f' {val}' for val in range(nb_col)] #on genere un tableau contenant chaque nombre au format ' {nombre}', en melangeant liste en comprehension et formatted string : c'est la maniere la plus proche que j'ai trouve d'avoir une string en comprehension
    for elt in tab:
        line += elt #on ajoute chaque element a la liste qui sera renvoyee
    return line


def affiche_grille(grille: list) -> None:
    """
        fonction qui affiche la grille complete dans le terminal

        on lui passe en entree la grille sous forme d'une matrice (tableau de tableau d'entiers), et elle l'affiche,
        avec des separateurs verticaux '|' entre les caracteres (colonnes), et horizontaux '+-+' entre les lignes
        etant donne la fonction boucle principale, cette fonction est appelee par le programme avec des valeurs 
        en entree (càd une grille) valides : la fonction ne gere donc pas les cas d'erreurs (erreur de type, de signe...), elle n'est pas reellement faite pour etre appelee manuellement    
        
        Cependant, l'argument attendu est une liste de listes d'entiers.

        attention cependant aux sous-listes trop importantes qui detraquent legerement le fonctionnement de l'affichage, le rendant moins propre au niveau de l'indication des colonnes (des qu'il y a plus de 10 colonnes)
        Le jeu reste cependant totalement fonctionnel, seul l'affichage est impacte (mais corriger ce probleme reviendrait a ne plus respecter les conventions etablies sur le sujet) 

    exemple :

    tableau de 7 colonnes et 6 lignes
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
    
    tableau de 7 colonnes et 10 lignes
    >>> affiche_grille(generer_grille_vide(7,10))
    +-+-+-+-+-+-+-+
    | | | | | | | |
    +-+-+-+-+-+-+-+
    | | | | | | | |
    +-+-+-+-+-+-+-+
    | | | | | | | |
    +-+-+-+-+-+-+-+
    | | | | | | | |
    +-+-+-+-+-+-+-+
    | | | | | | | |
    +-+-+-+-+-+-+-+
    | | | | | | | |
    +-+-+-+-+-+-+-+
    | | | | | | | |
    +-+-+-+-+-+-+-+
    | | | | | | | |
    +-+-+-+-+-+-+-+
    | | | | | | | |
    +-+-+-+-+-+-+-+
    | | | | | | | |
    +-+-+-+-+-+-+-+
     0 1 2 3 4 5 6
    
    tableau non valide :
    >>> affiche_grille([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],\
        [0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,3]])
    Traceback (most recent call last):
    ...
    ValueError: erreur de caractere
    """
    sep_hor = sep_lig(len(grille[0])) #separateur horizontal : +-+
    for lig in grille[::-1]: #on va parcourir dans le sens inverse.
        print(sep_hor) #on affiche le separateur horizontal
        print(gen_lig(lig)) #on affiche la ligne
    print(sep_hor)
    print(end_line(len(grille[0]))) #on affiche les numeros de colonne



#code 3

def peut_jouer(grille: list, colonne: int) -> bool: 
    """
        fonction renvoyant True si le coup donnee en argument est realisable : il ne l'est pas si la colonne associee est remplie (= si le dernier element de la colonne est occupe) ou si la colonne precisee n'existe pas.
    exemple:

    si le coup est faisable : 
    >>> peut_jouer([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],\
        [0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]], 2)
    True

    si le coup n'est pas faisable :
    >>> peut_jouer([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],\
        [0,1,2,2,0,0,0],[1,1,2,1,2,1,1]], 2)
    False

    si le coup n'est pas valide :
    >>> peut_jouer([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],\
        [0,1,2,2,0,0,0],[0,1,2,1,0,0,0]], 130)
    False
    """
    if colonne < len(grille[-1]):
        return (grille[-1][colonne] == 0) #on verifie seulement la derniere liste (la plus haute donc), si cela renvoie False c'est que la ligne est pleine
    return False #dans le cas ou le numero de colonne est superieur a la longueur de la liste, on a forcement un coup non valide



#code 4

def joue(grille: list, colonne: int, joueur: int) -> None:
    """
        fonction qui modifie le tableau grille dans la colonne en entree, placant le numero du joueur dans la ligne la plus basse possible    
        en considerant le coup possible (selon la fonction boucle_principale, cette fonction n'est appelee que si le coup est jouable)

        ici, pas de test a fournir
    """
    i = len(grille) - 1
    while i > 0 and grille[i-1][colonne] == 0:
        print(i)
        i -= 1
    grille[i][colonne] = joueur
    


#code 5

def a_gagne_vert(grille: list, joueur: int) -> bool:
    """
        fonction qui verifie verticalement la victoire du joueur passe en entree, renvoyant True si il existe une combinaison verticale du numero du joueur dans le tableau

        on a donc :
        -grille, une liste de liste d'entiers appartenant a {0,1,2} ;
        -joueur, un entier appartenant a {1,2}

        ici encore, on ne verifie pas les valeurs, la fonction etant appelee par la boucle principale avec des valeurs forcement vraie;
        cependant, a moins d'une erreur de type TypeError (mauvais type en entree) ou IndexError (tableau non valide) qui n'arrive pas lors de la boucle principale,
        pas d'erreur possible, juste un fonctionnement inutile :

        exemple :
    2 cas valides :
    >>> a_gagne_vert([[1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 1)
    True

    >>> a_gagne_vert([[1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 2)
    False

    2 cas "non valide"
    >>> a_gagne_vert([[1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 4)
    False

    >>> a_gagne_vert([[1,3,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 1)
    True

    erreur possible en cas d'appel manuel:

    >>> a_gagne_vert([[1,0,0,0,0,0,2], [1,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 2)
    Traceback (most recent call last):
    ...
    IndexError: list index out of range
    """
    nb_lig = len(grille)
    nb_col = len(grille[-1])
    if nb_lig >=4:
        for i in range(nb_col):
            for j in range(nb_lig - 4):
                if grille[j][i] == joueur: #si on tombe sur un pion du joueur;
                    looked = j
                    align = 0
                    while looked < nb_lig and grille[looked][i] == joueur: #on verifie verticalement les elements suivants tant qu'ils correspondent
                        align += 1
                        looked += 1
                    if align == 4: #quand ils ne correspondent plus, on verifie si on en a bien parcouru 4
                        return True #si c'est le cas, c'est gagne !
    return False


def a_gagne_hor(grille: list, joueur: int) -> bool:
    """
        fonction qui verifie horizontalement la victoire du joueur passe en entree, renvoyant True si il existe une combinaison horizontale du numero du joueur dans le tableau

        on a donc :
        -grille, une liste de liste d'entiers appartenant a {0,1,2} ;
        -joueur, un entier appartenant a {1,2}

        ici encore, on ne verifie pas les valeurs, la fonction etant appelee par la boucle principale avec des valeurs forcement vraie;
        cependant, a moins d'une erreur de type TypeError (mauvais type en entree) ou IndexError (tableau non valide) qui n'arrive pas lors de la boucle principale,
        pas d'erreur possible, juste un fonctionnement inutile :

        exemple :
    2 cas valides :
    >>> a_gagne_hor([[1,1,1,1,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 1)
    True

    >>> a_gagne_hor([[1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 2)
    False

    2 cas "non valide"
    >>> a_gagne_hor([[1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 4)
    False

    >>> a_gagne_hor([[3,3,3,3,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 3)
    True

    """
    nb_lig = len(grille)
    nb_col = len(grille[-1])
    if nb_col >= 4: #si on a pas de quoi gagner, on ne verifie meme pas si on a gagne;
        for i in range(nb_lig):
            for j in range(nb_col - 4):
                    if grille[i][j] == joueur: #meme principe que la fonction du dessus, mais horizontalement
                        looked = j
                        align = 0
                        while looked < nb_col and grille[i][looked] == joueur :
                            align += 1
                            looked += 1
                        if align == 4:
                            return True
    return False


def a_gagne_diag1(grille: list, joueur: int) -> bool:
    """
        fonction qui verifie sur la diagonale montante la victoire du joueur passe en entree, renvoyant True si il existe une combinaison sur la diagonale du numero du joueur dans le tableau

        on a donc :
        -grille, une liste de liste d'entiers appartenant a {0,1,2} ;
        -joueur, un entier appartenant a {1,2}

        ici encore, on ne verifie pas les valeurs, la fonction etant appelee par la boucle principale avec des valeurs forcement vraie;
        cependant, a moins d'une erreur de type TypeError (mauvais type en entree) ou IndexError (tableau non valide) qui n'arrive pas lors de la boucle principale,
        pas d'erreur possible, juste un fonctionnement inutile :

        exemple :
    2 cas valides :
    >>> a_gagne_diag1([[1,1,1,1,0,0,0], [1,1,0,0,0,0,0], [1,0,1,0,0,0,0], [1,0,0,1,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 1)
    True

    >>> a_gagne_diag1([[1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 2)
    False

    2 cas "non valide"
    >>> a_gagne_diag1([[1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 4)
    False

    >>> a_gagne_diag1([[3,3,3,3,0,0,0], [1,3,0,0,0,0,0], [1,0,3,0,0,0,0], [1,0,0,3,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 3)
    True

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


def a_gagne_diag2(grille: list, joueur: int) -> bool:
    """
        fonction qui verifie sur la diagonale descendante la victoire du joueur passe en entree, renvoyant True si il existe une combinaison sur la diagonale du numero du joueur dans le tableau

        on a donc :
        -grille, une liste de liste d'entiers appartenant a {0,1,2} ;
        -joueur, un entier appartenant a {1,2}

        ici encore, on ne verifie pas les valeurs, la fonction etant appelee par la boucle principale avec des valeurs forcement vraie;
        cependant, a moins d'une erreur de type TypeError (mauvais type en entree) ou IndexError (tableau non valide) qui n'arrive pas lors de la boucle principale,
        pas d'erreur possible, juste un fonctionnement inutile :

        exemple :
    2 cas valides :
    >>> a_gagne_diag2([[0,0,0,1,0,0,0], [0,0,1,0,0,0,0], [0,1,0,0,0,0,0], [1,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 1)
    True

    >>> a_gagne_diag2([[1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 2)
    False

    2 cas "non valide"
    >>> a_gagne_diag2([[1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 4)
    False

    >>> a_gagne_diag2([[0,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,3], [1,0,0,0,0,3,0], [0,0,0,0,3,0,0], [0,0,0,3,0,0,0]], 3)
    True

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


def a_gagne(grille: list, joueur: int) -> bool:
    """
        fonction qui verifie la victoire du joueur dans toutes les directions, renvoyant True si il existe une combinaison du numero du joueur dans le tableau

        on a donc :
        -grille, une liste de liste d'entiers appartenant a {0,1,2} ;
        -joueur, un entier appartenant a {1,2}

        ici encore, on ne verifie pas les valeurs, la fonction etant appelee par la boucle principale avec des valeurs forcement vraie;
        cependant, a moins d'une erreur de type TypeError (mauvais type en entree) ou IndexError (tableau non valide) qui n'arrive pas lors de la boucle principale,
        pas d'erreur possible, juste un fonctionnement inutile.

        comme on execute les 4 fonctions precedentes, les resultats sont les "memes" : si une des fonctions renvoie True, on renvoie True.
    
    exemple (pour des exemples plus precis, voir les 4 fonctions precedentes) :

    >>> a_gagne([[0,0,0,1,0,0,0], [0,0,1,0,0,0,0], [0,1,0,0,0,0,0], [1,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 1)
    True
    >>> a_gagne([[1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [1,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 1)
    True
    >>> a_gagne([[1,1,1,1,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 1)
    True
    >>> a_gagne([[1,1,1,1,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]], 2)
    False
    """
    return ((a_gagne_vert(grille, joueur) or a_gagne_hor(grille, joueur)) or (a_gagne_diag1(grille, joueur) or a_gagne_diag2(grille, joueur)))



#code 6

def grille_pleine(grille: list) -> bool:
    """
        fonction verifiant si la grille passee en argument est remplie ou non :
        si elle est pleine, alors la derniere ligne est remplie, c'est pourquoi on ne verifie que celle-ci

        on passe en argument une liste de listes d'entiers qu'on considere realisee par le programme : ne contenant que des 0, 1 et 2 ; aux listes remplies progressivement (la derniere n'est completement remplie que si les autres le sont)

        exemple :

        grille completement remplie par le programme (donc, valide):
        >>> grille_pleine([[1,2,1,2,2,1,1],[1,2,1,2,2,1,1],[1,2,1,2,2,1,1],[1,2,1,2,2,1,1],[1,2,1,2,2,1,1],[1,2,1,2,2,1,1]])
        True

        grille non remplie mais valide :
        >>> grille_pleine([[1,2,1,2,2,1,1],[1,2,1,2,2,1,1],[1,2,1,2,2,1,1],[1,2,1,2,2,1,1],[1,2,1,2,2,1,1],[0,0,0,0,0,0,0]])
        False

        2 exemples non valides :

        grille non remplie mais manuellement creee :
        >>> grille_pleine([[1,2,1,2,2,1,1],[1,2,1,2,2,1,1],[1,2,100,3,2,1,1],[0,0,0,0,0,0,0],[1,2,1,2,2,1,1],[0,0,0,0,0,0,0]])
        False

        idem, grille non remplie mais manuellement creee :
        >>> grille_pleine([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,2,1,2,2,1,1]])
        True

    """
    for elt in grille[-1]:
        if elt == 0:
            return False
    return True



#code 7

def boucle_principale(nb_col = 7, nb_lig = 6) -> int: #on precise des valeurs qui seront utilisees si aucune ne sont donnees
    """
        fonction principale du jeu, celle que l'on appelle pour lancer une partie. Elle recoit en entree 2 arguments, nb_col et nb_lig, qui sont 2 entiers definissant le format de la grille de jeu.
        Si on ne fournit pas d'argument, c'est la taille classique qui est mise en place.
        en cas d'arguments ne permettant pas d'avoir les 3 cas de victoire (diagonale, horizontale ou verticale), c'est a dire si l'un des arguments est inferieur a 4, on demande confirmation des parametres
        de meme, si le nombre de colonne est superieur a 10, on demande confirmation (car en respectant les conventions du sujet, cela entraine quelques problemes d'affichage rendant le tout moins lisible)
        (d'autant plus que techniquement, la boucle principale ne demandait pas une taille precise)

        Comme c'est cette fonction qui est appelee par l'utilisateur, si elle est executee on est sur d'avoir des parametres valides pour les sous-fonctions (d'ou une gestion des erreurs plus 'legere' dans les autres fonctions)

        en effet, la grille sera toujours remplie correctement par de bonnes valeurs, les joueurs seront toujours les bons...

        (pas de doctest a fournir ici)

        dans le cadre d'une potentielle gestion de partie, on renvoie le numero du gagnant en cas de victoire, 0 en cas de defaite (on peut imaginer une fonction qui execute a nouveau une partie en cas d'ex aequo, un simili tournoi en plusieurs parties...) 
    """
    while nb_lig < 4 or nb_col < 4 :
        print(f"attention : la grille actuelle ({nb_lig} lignes et {nb_col} colonnes ne permet pas de mener une partie convenable.")
        if nb_lig > 0 and nb_col > 0 :
            continuer = input("voulez-vous conserver ces parametres ? y/n ")
            if continuer == 'y':
                print(f'tres bien on continue avec une grille de {nb_lig} lignes et {nb_col} colonnes \n')
                break #comme on conserve les valeurs actuelles qui ne repondent pas aux exigences classiques, on sort de la boucle avec 'break'
        print("definitions de nouvelles valeurs : \n")
        nb_lig = int(input("combien de lignes ? "))
        nb_col = int(input("combien de colonnes ? "))
    
    grille = generer_grille_vide(nb_col, nb_lig)
    joueur_courant = 1

    while not grille_pleine(grille):
        affiche_grille(grille)
        coup = (input(f"quel est ton prochain coup, joueur {joueur_courant} ? "))
        while (coup not in [str(i) for i in range(nb_col)]) or (not peut_jouer(grille, int(coup))) : #on s'assure que le coup est bien convertissable en entier et qu'il est bien valide
            print("erreur ! le coup n'est pas valide \n")
            affiche_grille(grille)
            coup = (input("\nprière de redonner un coup valide :\n"))
        coup = int(coup) #on convertit le coup qui est sur d'etre convertissable pour pouvoir l'utiliser
        joue(grille, coup, joueur_courant)
        if a_gagne(grille, joueur_courant):
            affiche_grille(grille)
            print(f"tu as gagné joueur {joueur_courant} ! Félicitations !")
            return joueur_courant
        joueur_courant = (joueur_courant % 2) + 1 #si joueur courant = 1, alors on a 1 + 1 = 2 ; si joueur courant courant = 2, alors 0 + 1 = 1
    print("ex aequo ! il n'y a pas de gagnant cette fois-ci...")
    return 0




if __name__ == "__main__":
    doctest.testmod(verbose=True)

    ##ci-dessous, des tests plus en details un peu redondant avec les doctests, que je laisse surtout pour avoir des arguments definis (plus pratique en cas de test plus pousse)
    '''print("test d'affichage \n")
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
    print(grille_pleine(filled_grid))'''


    print("\n\n\n\n test du jeu \n\n")
    boucle_principale()

