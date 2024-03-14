from utils_client import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentece = input('Input lowercase sentece:')
clientSocket.send(sentece.encode())
modifiedSentece = clientSocket.recv(1024)
print('From Server: ', modifiedSentece.decode())
clientSocket.close()