# coding=utf-8
import socket

server = ("192.168.1.6", 9998)
# socket.AF_INET IPv4   SOCK_STREAM THHP协议
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server)
sock.listen(5)  # 监听5个请求
conn, address = sock.accept()
print "connect by ", address
while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data)
    conn.send(data)

conn.close()
