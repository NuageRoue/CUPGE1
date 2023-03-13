import socket as soc

IP = "127.0.0.1"
PORT = 8080

socket_serveur = soc.socket(soc.AF_INET, soc.SOCK_DGRAM)
socket_serveur.bind((IP,PORT))

while True:
    data, addr = socket_serveur.recvfrom(65536)

    data = data.decode()
    print(data)

    MESSAGE_RETOUR = "reveive " + data
    socket_serveur.sendto(MESSAGE_RETOUR.encode(), addr)
