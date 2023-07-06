import socket as soc
import threading
## definition des constantes :

BALISE_NEW_NAME = "__new_name__:"
BALISE_MESSAGE = "__message__:"
BALISE_QUIT = "__quit__"
BALISE_ERROR = "__error__:"
IP = "127.0.0.1"
PORT = 5050

socket_client = soc.socket(soc.AF_INET, soc.SOCK_DGRAM)


def chooseUsername():
    username = input("nom d'utilisateur : ")
    message = f"{BALISE_NEW_NAME} {username}"
    socket_client.sendto(message.encode(),(IP,PORT))


def handleError(errorType):
    """
        fonction reagissant a l'erreur renvoye par le serveur, selon 3 modeles :

            - AlreadyHereError : le client envoie un pseudo mais est deja identifie ; aucun traitement necessaire.
            - IdentificationError : le client envoie un message (ou une notification de deconnexion) mais n'est pas enregistre aupres du serveur : il doit donc s'identifier.
            - NameError : le client envoie un pseudo (ou une notification de deconnexion) mais celui-ci est deja utilise : il doit donc en changer.
    """
    match errorType:
        case "IdentificationError":
            print("Attention: vous n'êtes pas connecté : prière de choisir un nom d'utilisateur.")
            chooseUsername()
        case "NameError":
            print("Attention: ce nom d'utilisateur est déjà utilisé : prière de choisir un nouveau nom d'utilisateur.")
            chooseUsername()



def send():
    chooseUsername()
    while True :
        balise = BALISE_MESSAGE
        message = input()
        if message == 'quit':
            socket_client.sendto(BALISE_QUIT.encode(),(IP,PORT))
            break
        elif message.replace(" ","") != "":
            toSend = f"{balise} {message}"
            socket_client.sendto(toSend.encode(),(IP,PORT))

def receive():
    while True:
        data, addr = socket_client.recvfrom(65526)
        data = data.decode()
        baliseReceived = data.split(' ')[0]
        if baliseReceived == BALISE_QUIT:
            socket_client.close()
            break
        elif baliseReceived == BALISE_ERROR:
            handleError(data.split(' ')[1])
        else:
            print(data)



# Cr´eation des processus
send_thread = threading.Thread ( target = send )
recv_thread = threading.Thread ( target = receive )
# Lancement des processus
send_thread.start()
recv_thread.start()


