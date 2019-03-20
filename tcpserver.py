from socket import *
serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("the server is ready to receive")
while True:
    connectionSocket,addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    sentence = sentence.upper()
    connectionSocket.send(sentence.encode())
    connectionSocket.close()