from socket import *
serverName = '0-pc'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_DGRAM)#底层网络使用ipv4,类型为UDP
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedmessage, serverAddress = clientSocket.recvfrom(2048)#2048为缓存长度
print(modifiedmessage.decode())
print(serverAddress)
clientSocket.close()