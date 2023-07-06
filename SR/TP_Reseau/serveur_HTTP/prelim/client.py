import socket as sct
IP = "127.0.0.1"
PORT = 8080

socket_client = sct.socket(sct.AF_INET, sct.SOCK_STREAM)
MESSAGE = "GET /pages/index.html HTTP/1.1\r\nHost: localhost\r\nAccept-Language: fr\r\n\r\n".encode()

socket_client.connect((IP, PORT))

socket_client.send(MESSAGE)
data = socket_client.recv(65535)

print(data.decode())

socket_client.close()
