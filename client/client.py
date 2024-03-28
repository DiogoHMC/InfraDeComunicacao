from utils_client import *

serverName = '127.0.0.1'
serverPort = 12000

while True:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    sentence = input('Input lowercase sentece: ')
    clientSocket.send(sentence.encode())
    modifiedSentece = clientSocket.recv(1024)
    print('From Server: ', modifiedSentece.decode())

    if sentence == 'exit':
        break

    clientSocket.close()