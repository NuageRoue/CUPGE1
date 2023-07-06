import socket as soc
import serveurHTTP as serv


serveur = soc.socket(soc.AF_INET, soc.SOCK_STREAM)

serveur.bind(("127.0.0.1", 8080))

while True:
    serveur.listen()
    socket_client, addr = serveur.accept() # socket client et son adresse
    print(addr)
    data = socket_client.recv(65535) # données transmises
    print(serv.traite_requete(data.decode()))
    
    socket_client.send("Bien reçu !".encode())
