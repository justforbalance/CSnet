from socket import *
serverName = '0-pc'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input("input lowercase sentence")
clientSocket.send(sentence.encode())#字符串转化为字节类型
modifiedSentence = clientSocket.recv(1024)
print("from server:", modifiedSentence.decode())
clientSocket.close()
