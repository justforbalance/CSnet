"""
使用socket连接baidu
1. 创建一个ipv4 + tcp的socket
2. socket建立tcp连接, tcp连接只用指明域名（ip）+ 端口
3. 发送内容, 这里发送的是http协议的报文
4. 接受相应==响应数据每次接收1024字节
5. 关闭socket
"""
import socket

# 1. 创建一个ipv4 + tcp的socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 建立tcp连接
s.connect(('www.baidu.com', 80))

# 3. 发送http协议的报文
http_message = b'GET / HTTP/1.1\nHost: www.baidu.com\nConnection: close\n\n'
s.send(http_message)

# 4. 接受响应数据
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

# 5. 关闭socket
s.close()

# 6. 将数据用utf-8解码, 存入文件观察
data = (b"".join(buffer)).decode("utf8")
with open("baidu", 'w', encoding="utf8") as f:
    f.write(data)