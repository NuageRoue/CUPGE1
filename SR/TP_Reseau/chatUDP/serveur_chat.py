import socket as soc

## definition des constantes :

BALISE_NEW_NAME = "__new_name__:"
BALISE_MESSAGE = "__message__:"
BALISE_QUIT = "__quit__"
BALISE_ERROR = "__error__:"
IP = "127.0.0.1"
PORT = 5050

socket_serveur = soc.socket(soc.AF_INET, soc.SOCK_DGRAM)
socket_serveur.bind((IP,PORT))
adresses = {}

def send_entrance_notification(addr, name):
    """
        fonction envoyant a tous les clients connectes une notification indiquant qu'un nouveau client est connecte, en leur envoyant le pseudo de son choix
    """
    if addr not in adresses : # on verifie que le client n'est pas deja identifie ;
        for adr in adresses: # si ce n'est pas le cas, on verifie que le nom demande par le nouveau client n'est pas deja attribue
            if adresses[adr] == name:
                 socket_serveur.sendto(f"{BALISE_ERROR} NameError".encode(), addr) # si il l'est deja, on envoie une erreur au client et on stoppe le processus de notifications
                 return -1
        adresses[addr] = name #sinon, on enregistre le nouveau client;
        for adr in adresses : # et on notifie tout le monde de l'arrivee du nouveau client
            socket_serveur.sendto(f"\n***{name}*** vient de rentrer sur le chat !\n".encode(), adr)
    else:
        socket_serveur.sendto(f"{BALISE_ERROR} AlreadyHereError".encode(), addr) # si le client est deja identifie, on envoie une erreur au client
        return -1

def send_message(addrExp, message):
    """
        fonction envoyant a tous les utilisateurs (sauf l'expediteur) le message recu par le serveur. 
    """

    if addrExp not in adresses: # on verifie que l'expediteur fait bien parti du dictionnaire d'adresses ;
        socket_serveur.sendto("IdentificationError".encode(), addrExp) #sinon on le notifie d'une erreur d'identification avant de stopper l'execution.
        print('IdentificationError')
        return -1
    for addr in adresses: #si tout se passe bien, on envoie a tous sauf a l'expediteur le message envoye par le client
        print(addr)
        if addr != addrExp:
            socket_serveur.sendto(f"[{adresses[addrExp]}] : {message}".encode(), addr)

def send_quit_notification(addrExp):
    """
        fonction envoyant une notification de deconnexion d'utilisateur a tous les autres utilisateurs
    """
    if addrExp not in adresses: # on verifie que l'expediteur fait bien parti du dictionnaire d'adresses ;
        socket_serveur.sendto("IdentificationError".encode(), addrExp) # sinon on le notifie d'une erreur d'identification avant de stopper l'execution.
        return -1
    #si tout se passe bien :
    socket_serveur.sendto(BALISE_QUIT.encode(), addrExp) # on renvoie a celui qui se deconnecte une balise quit, pour arreter le thread "receive"
    pseudo = adresses[addrExp]
    del adresses[addrExp] # on supprime l'expediteur du dictionnaire
    for addr in adresses:
            socket_serveur.sendto(f"***{pseudo}*** a quitté le chat".encode(), addr) #on notifie tous les utilisateurs restants de la deconnexion de l'un
    



def traite_data(addr, data):
    baliseReceived = data.split(' ')[0]
    message = ' '.join(data.split(' ')[1:])
    if baliseReceived == BALISE_NEW_NAME: 
        send_entrance_notification(addr, message)
    elif baliseReceived == BALISE_MESSAGE: 
        send_message(addr, message)
    elif baliseReceived == BALISE_QUIT: 
        send_quit_notification(addr)
    else :
        socket_serveur.sendto(f"{BALISE_ERROR} BaliseError".encode(), addr)
        return -1


while True:
    data, addr = socket_serveur.recvfrom(65536)

    data = data.decode()
    print(data)
    traite_data(addr,data)