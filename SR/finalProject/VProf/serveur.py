import socket as soc
from random import choice

## definition des constantes :
BALISE_NEW_NAME = "__new_name__:"
BALISE_MESSAGE = "__message__:"
BALISE_MOVE = "__move__:"
BALISE_END = "__end__:"
IP = "127.0.0.1"
PORT = 5050

socket_serveur = soc.socket(soc.AF_INET, soc.SOCK_DGRAM)
socket_serveur.bind((IP,PORT))
addrDict = {}
addrList = []


# fonction pour la generation de la grille sous forme de chaine de caractere :

def EndLine(nb:int) -> str: 
    """
        fonction generant une ligne de lettres pour conclure la grille; elle recoit en entree la longueur d'une ligne de la grille (I.E. le nombre de colonne a nommer)

        Il faut donc un nombre de colonne inferieur a 26 (les 26 lettres de l'alphabet...), mais c'est le cas avec les parametres de base
    """
    line = " " * (NbDigit(nb - 1) + 1) # tous les espaces au debut
    for i in range(nb):
        line += " "+chr(ord("A")+i) # on ajoute toutes les lettres correspondants a toutes les colonnes
    return "\n" + line + "\n" # on renvoie la ligne avec un newline avant et apres

def NbDigit(nb:int) -> int:
    """
        fonction retournant le nombre de chiffre composant l'entier nb passe en argument ;
    """
    i = 1
    while (nb//10): # tant que la partie entiere de la division du nombre par 10 n'est pas nulle :
        nb //= 10 # on retire le premier chiffre a droite en effectuant cette division ;
        i += 1 # on incremente notre compteur de chiffre.
    return i

def Line(nb:int, gridLine:list, nbMax=10) -> str:
    """
        fonction qui specifiquement genere sous forme de string la liste gridLine, representant une ligne de la grille
        on specifie un numero de taille maximale afin de parfaire l'affichage (si on a comme taille maximale un nombre a 2 chiffres, on ajoutera un espace a ceux n'ayant qu'un chiffre)

        nb est donc un entier correspondant a la position de la ligne dans la grille (avec les parametres de base, de 0 a 14);
        gridLine une liste de 15 elements ;
        nbMax est specifie a 10 de base, mais il peut etre modifie (et doit l'etre des que l'on a une grille de 100 elements par ligne)    
    """
    charList = [".","X","O"] # la liste des caracteres a afficher ;
    line = (NbDigit(nbMax) - NbDigit(nb)) * " " + f"{nb}|" # on commence par ajouter notre chiffre au debut de la ligne, avec suffisamment d'espace " " pour ne pas causer de decalage plus tard : on en ajoute autant qu'il manque de chiffre a notre nombre pour arriver au nombre maximal
    for i in gridLine:
        line += (" " + charList[i]) # on ajoute a la ligne le caractere correspondant a l'element de la ligne 
    return line+"\n"

def GridShow(grid:list) -> str:
    """
        fonction recevant en entree une liste de liste grid et renvoyant une chaine de caractere representant cette grille

        Tous les elements de cette matrice doivent etre des entiers allant de 0 a 2 pour gerer l'affichage (c'est forcement le cas dans le programme, donc sauf si elle est appelee seule)
    """
    strGrid = ""
    for i in range(len(grid)): # pour chaque numero de ligne :
        strGrid += Line(i, grid[i], len(grid)) # on ajoute toutes les lignes a la grille
    return strGrid + (" " * (NbDigit(len(grid) - 1) + 1)) + ("-" * 2 * len(grid)) + EndLine(len(grid)) # on ajoute aussi la ligne d'underscore et la ligne de lettre : 2 underscore pour chaque caracterem sans oublier les espaces au debut


def MakeGrid(width:int) -> list:
    """
        fonction generant une matrice de taille width * width composee de 0
    """
    if width < 10:
        width = 10
    return [[0 for i in range(width)]for j in range(width)]

def CanPlay(grid:list) -> bool:
    """
        fonction prenant en entree une matrice representant la grille de jeu et :
        - renvoyant True si il est encore possible de jouer (s'il reste au moins un 0 dans la matrice)
        - sinon, False
    """
    for line in grid:
        for elt in line:
            if elt == 0:
                return True
    return False

def MoveIsValid(move:str):
    """
        fonction recevant en entree une representation sous forme de chaine de caractere d'une case de la grille, et renvoyant un tuple compose de :
        False et None si le coup n'est pas valide (I.E. si la case est :
                                                                        - deja occupee;
                                                                        - n'existe pas dans la grille
                                                                        - si le coup ne represente pas une grille)
    """
    if move[0].isupper() and move[1::].isdigit():# le coup se compose d'une lettre majuscule representant la colonne, et un nombre representant la colonne, si c'est le cas :
        line = int(move[1::]) #on recupere ligne et colonne en chiffres ;
        col = ord(move[0]) - ord("A")
        if (line < len(grid) and col < len(grid)) and grid[line][col] == 0: # si cette ligne et cette colonne font parti de la grille :
            return True,(line,col) # on renvoie True, et la ligne et la colonne ;
    return False,None #sinon, on renvoie False,None



def Play(player:int, move:tuple):
    """
        fonction simple modifiant notre grille en attribuant la valeur player (1 ou 2 sauf si appelee seule) a la case de coordonnees move
    """
    grid[move[0]][move[1]] = player



#verification de la victoire d'un joueur : specifique au serveur
def WinVert(grid:list,player:int)->bool:
    """
        fonction verifiant verticalement la victoire du joueur player dans la grille grid : on verifie si on a 5 chiffres player se suivant verticalement
    """
    lenGrid = len(grid)
    for j in range(lenGrid):
        for i in range(lenGrid):
            if grid[i][j] == player:#si on tombe sur le chiffre recherche :
                looked = i
                align = 0
                while looked < lenGrid and grid[looked][j] == player: # on parcourt le reste de la ligne tant qu'on retrouve le meme chiffre ;
                    align += 1
                    looked += 1
                if align == 5: #quand ils ne correspondent plus, on verifie si on en a bien parcouru 4
                        return True #si c'est le cas, c'est gagne !
    return False

def WinHor(grid,player):
    """
        fonction verifiant horizontalement la victoire du joueur player dans la grille grid : on verifie si on a 5 chiffres player se suivant verticalement
    """
    lenGrid = len(grid)
    for line in grid:
        for i in range(lenGrid):
            if line[i] == player: #comme sur la fonction precedente mais sur la ligne
                looked = i
                align = 0
                while looked < lenGrid and line[looked] == player:
                    looked += 1
                    align += 1
                if align == 5:
                    return True
    return False

def WinDiag1(grid, player):
    """
        fonction qui verifie sur la diagonale montante la victoire du joueur passe en entree, renvoyant True si il existe une combinaison sur la diagonale du numero du joueur dans le tableau
    """
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

def Win(grid:list, player:int):
    """
        on appelle les 4 fonctions precedentes pour renvoyer un booleen correspondant au fait que le joueur gagne (ou non)
    """
    return ((WinVert(grid, player) or WinHor(grid, player)) or (WinDiag1(grid, player) or WinDiag2(grid, player)))


# fonction de traitement :

def NewPlayer(name:int, addr:tuple):
    """
        fonction enregistrant un joueur si jamais 2 joueurs ne sont pas enregistres : name est une string correspondant a son pseudo, addr le tuple compose de son adresse ip et de son port ;

        Toutefois, si 2 joueurs sont deja enregistres, elle envoie un message ;

        les 2 arguments sont recus par le socket serveur, normalement cette fonction n'est pas appelee seule pour eviter les erreurs ;
    """
    if len(addrList) < 2: # on s'assure de ne pas deja avoir enregistre 2 joueurs
        addrDict[addr] = name # on associe adresse et pseudo dans le dictionnaire addrDict ;
        addrList.append(addr) # on enregistre l'adresse seule dans la liste addrList (qui simplifiera le code ulterieurement)
        socket_serveur.sendto(f"Bienvenue {name} !".encode(), addr) # on envoie un message de bienvenue au joueur
    else: 
        socket_serveur.sendto(f"Il y a deja 2 joueurs...".encode(), addr) # si on a deja 2 joueurs, on envoie un message au joueur essayant de se connecter.

def SendMessage(data:str, addr:tuple,balise = BALISE_MESSAGE):
    """
        fonction envoyant au client d'adresse addr le message data, precede de la balise balise (BALISE_MESSAGE par defaut)

        addr provient de la liste d'adresses deja recus, normalement cette fonction n'est pas appelee seule pour eviter les erreurs ;
    """
    socket_serveur.sendto((balise+data).encode(), addr)

def SendAll(data:str,balise = BALISE_MESSAGE):
    """
        fonction envoyant a tous les clients le message data precede de la balise balise (BALISE_MESSAGE par defaut)
    """
    for player in addrList:
        SendMessage(data, player,balise)

def BeginGame(data:str,addr:tuple) -> int :
    """
        fonction gerant le debut du jeu (tant que les 2 joueurs ne sont pas enregistres et identifies)

        on recoit en entree data et addr (les 2 arguments sont recus par le socket serveur) et on effectue le traitement necessaire
    """
    if data.startswith(BALISE_NEW_NAME): # si on reciot un message d'identification commencant par la balise NEW_NAME :
        NewPlayer(":".join(data.split(":")[1::]),addr) # on appelle la fonction NewPlayer avec en entree data (sans la balise, l'encapsulation de join et split permettant de ne garder que la fin) et addr
    elif data.startswith(BALISE_MOVE) and addr in addrList: # si on recoit un message commencant par la balise NEW_MOVE de la part d'un joueur deja enregistre :
        SendMessage("Ce n'est pas votre tour !",addr) # on lui envoie un message indiquant que ce n'est pas son tour
    else:
        SendMessage("erreur : message non reconnu",addr) # si le joueur n'est pas identifie et envoie autre chose qu'un  message d'identification commencant par la balise NEW_NAME, on lui indique que son message est b=non reconnu ;
    if len(addrList) == 2 : # une fois le 2eme joueur enregistre, on commence le jeu :
        current = choice([0,1]) #on choisi un joueur au hasard
        currentAddr = addrList[current]
        SendAll(GridShow(grid)) # on envoie a tous la grille ;
        SendMessage(f"joueur {addrDict[currentAddr]}, quel est votre coup ?",currentAddr) # et on indique au joueur courant qu'on attend son coup
        return current # on renvoie sa position dans la liste addrList
    return 0 #on renvoie 0 si la fonction doit encore etre appelee

def TraiteData(data:str,addr:tuple,current:int):
    """
        fonction principale, gerant le jeu a partir du moment ou tous sont identifies ;

        on recoit en entree data et addr (les 2 arguments sont recus par le socket serveur) et l'indice dans addrList du joueur courant, et on effectue le traitement necessaire

        on renvoie un entier etant soit l'indice du joueur courant dands la liste addrList, soit -1 si le jeu est fini ;
    """
    currentAddr = addrList[current]
    if data.startswith(BALISE_NEW_NAME): # si le message recu commence par la balise NEW_NAME, on indique au joueur qu'il y a deja 2 joueurs (si on a le bon client, cela n'arrive qu'avec un client modifie)
        SendMessage("Il y a deja 2 joueurs...",addr)
    elif data.startswith(BALISE_MOVE): # s'il commence par la balise MOVE :
        if addr not in addrList: # si le client n'est pas l'un des joueurs, on le lui indique
            SendMessage("Vous ne faites pas parti des joueurs !",addr)
        elif addr != currentAddr: # si on n'a pas affaire au joueur courant : 
            SendMessage("Ce n'est pas a vous de jouer !", addr)
        else:
            move = ":".join(data.split(":")[1::]) # on recupere le coup sans la balise ;
            if MoveIsValid(move)[0]: #si il est valide,
                Play(current+1,MoveIsValid(move)[1]) # on modifie la grille
                SendAll(GridShow(grid)) #on envoie a tous la grille modifiee puis :
                if Win(grid, current+1): #on verifie si le jeu peut continuer 
                    SendAll(f"{addrDict[addr]} a gagne !",BALISE_END) #si le jeu est fini, on envoie a tous un message indiquant la victoire du joueur courant (avec la balise END qui provoque l'appel a une fonction qui indique que le jeu est fini)
                    return -1 # on renvoie -1, ce qui met fin a la boucle du serveur
                elif CanPlay(grid): #sinon si on peut toujours jouer :
                    current = (current+1) % 2 # on passe au joueur suivant ;
                    currentAddr = addrList[current] 
                    SendMessage(f"joueur {addrDict[currentAddr]}, quel est votre coup ?",currentAddr) # on demande son coup au nouveau joueur courant
                else:
                    SendAll("La grille est pleine : match nul !",BALISE_END) # si la grille est pleine, on met fin a la partie (balise end, -1 en valeur de retour)
                    return -1
            else:
                SendMessage("Coup Invalide !",addr) # si le coup n'est pas valide, on l'indique
    return current # si on a pas mis fin au jeu ou change de joueur courant, on renvoie l'indice du joueur courant actuel.

current = 0 # on initialise la valeur du joueur courant a 0
grid = MakeGrid(15) # on genere la grille ;
while current != -1: # tant que le jeu ne prend pas fin en attribuant la valeur -1 a l,indice du joueur courant ; 
    data,addr = socket_serveur.recvfrom(65536) # on recupere message et adresse recus ;
    data = data.decode() # on decode les donnees recues
    if len(addrList) < 2: # si nos 2 joueurs ne sont pas encore identifies:
        current = BeginGame(data,addr) # on appelle BeginGame
    else:
        current = TraiteData(data,addr,current) #sinon on appelle TraiteData;
