import socket as soc
import threading

## definition des constantes :
BALISE_NEW_NAME = "__new_name__:"
BALISE_MESSAGE = "__message__:"
BALISE_MOVE = "__move__:"
BALISE_END = "__end__:"
IP = "127.0.0.1"
PORT = 5050

socket_client = soc.socket(soc.AF_INET, soc.SOCK_DGRAM)


def chooseUsername(): 
    """
        fonction appelee en premiere dans le thread send, elle demande a l'utilisateur de rentrer un nom d'utilisateur ;
    """
    username = input("nom d'utilisateur : ")
    message = f"{BALISE_NEW_NAME}{username}"
    socket_client.sendto(message.encode(),(IP,PORT))

def send():
    """
        fonction du thread send, elle gere l'envoi des entrees du joueur au serveur.
    """
    chooseUsername()
    while True :
        message = input()
        if message.replace(" ","") != "": # si le message sans espace n'est pas vide :
            toSend = f"{BALISE_MOVE}{message}" # on prepare le message a l,envoi en y ajoutant la balise MOVE
            socket_client.sendto(toSend.encode(),(IP,PORT)) # on envoie au serveur notre message

def receive():
    """
        fonction du thread receive, elle gere la reception et l'affichage des messages du serveur.
    """
    while True:
        data, addr = socket_client.recvfrom(65526) # on recupere les donnees recues par le serveur;
        if addr == (IP,PORT):
            data = data.decode()
            if data.startswith(BALISE_END): # si le message commence par la balise END
                print(":".join(data.split(':')[1::])) # on affiche le message ;
                print("La partie est terminée ! (Appuyez sur Ctrl+C pour quitter)") # on affiche ce message
            elif data.startswith(BALISE_MESSAGE): #s'il s'agit d'un message simple;
                print(":".join(data.split(':')[1::])) # on l'affiche




# Creation des processus
send_thread = threading.Thread ( target = send )
recv_thread = threading.Thread ( target = receive )
# Lancement des processus
send_thread.start()
recv_thread.start()


