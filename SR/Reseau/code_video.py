import socket as sct

# socket : interface d'acces au reseau permettant l'usage d'un port logiciel alloue.
# caracterise par : un numero de portm une adresse IP et un protocole.





#declaration des sockets :
socket_TCP_IPV4 = sct.socket(sct.AF_INET, sct.SOCK_STREAM)
socket_UDP_IPV4 = sct.socket(sct.AF_INET, sct.SOCK_DGRAM)

ip_client = None
IP_SERVEUR = None
PORT_SERVEUR = None
donnees = None
taille_tampon = None


# cote client :
socket_client = sct.socket(sct.AF_INET, sct.SOCK_STREAM)

# ouverture du dialogue : toujours du cote client.
# attention, la connexion n'est faite qu'en TCP
socket_client.connect((IP_SERVEUR, PORT_SERVEUR))



#cote serveur
socket_serveur = sct.socket(sct.AF_INET, sct.SOCK_STREAM)

# cote serveur, il faut lier le socket a une IP et un port 
socket_serveur.bind((IP_SERVEUR, PORT_SERVEUR))
socket_serveur.listen() # on ecoute le port logiciel

#en TCP, il faut accepter la connexion :
client, (ip_client, port_client) = socket_serveur.accept() # on stocke en memoire les infos du client

# /!\ : serveur et client sont sur 2 mqchines differentes, et donc 2 programmes differents

#une fois la connexion etablie :
socket_client.send(donnees) # emission de donnees
data = socket_serveur.recv(taille_tampon) # reception de donnee : pas forcement par le serveur !

# en mode non connecte (UDP)
socket_client.sendto(donnees, (IP_SERVEUR, PORT_SERVEUR))
data = socket_serveur.recvfrom(taille_tampon)

socket_serveur.close() #pour fermer le socket 
