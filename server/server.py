from socket import *
serverPort = 12000

# Criação do Socket Servidor
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))

# Escutar para Receber Sentenças
serverSocket.listen(5)
print('The server is ready to receive')

while True:
    
    # Escutar Requesições do Cliente
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode ()
    print("Mensagem recebida:", sentence)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence .encode())
    connectionSocket.close()