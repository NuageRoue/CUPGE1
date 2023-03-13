import socket as sct

IP = "127.0.0.1" # ip du serveur
PORT = 8080 # port du serveur

socket_serveur = sct.socket(sct.AF_INET, sct.SOCK_STREAM) # definition d'un socket IPV4 TCP
socket_serveur.bind((IP, PORT)) # on va lier le socket au port et a l'IP definis plus haut

while True:
    socket_serveur.listen()
    socket_client, addr = socket_serveur.accept()
    data = socket_client.recv(65535)
    print(data.decode())
    socket_client.send("received".encode())

socket_serveur.close()



"""import socket as soc

IP = "127.0.0.1"
PORT = 8080

socket_serveur = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
socket_serveur.bind((IP,PORT))

while True:
    socket_serveur.listen()
    soc_client, addr = socket_serveur.accept()
    data = soc_client.recv(65536)

    data = data.decode()
    print(data)

    MESSAGE_RETOUR = "reveive " + data
    soc_client.send(MESSAGE_RETOUR.encode(), addr)
    socket_serveur.close()
"""
