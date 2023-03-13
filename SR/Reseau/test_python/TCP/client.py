import socket as sct

IP = "127.0.0.1"
PORT = 8080

socket_client = sct.socket(sct.AF_INET, sct.SOCK_STREAM)
MESSAGE = "Hello World !".encode()

socket_client.connect((IP, PORT))

socket_client.send(MESSAGE)
data = socket_client.recv(65535)
print(data.decode())

socket_client.close()




"""import socket as soc

IP = "127.0.0.1"
PORT = 8080

socket_client = soc.socket(soc.AF_INET, soc.SOCK_DGRAM)

MESSAGE = input("Entrer votre message ici : \n").encode()

socket_client.sendto(MESSAGE,(IP,PORT))

data, addr = socket_client.recvfrom(65526)

print(data.decode())"""
