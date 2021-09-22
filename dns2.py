import socket
#socket.getaddrinfo(host, port, family, type, proto, flags)
#None=localhost=127.0.0.1=ipv6adress  ,smtp=25,0,socket.SOCK_STREAM because smtp use TCP
info = socket.getaddrinfo(None,'smtp',0,socket.SOCK_STREAM,0,socket.AI_PASSIVE)
print(info)