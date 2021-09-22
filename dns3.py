import socket
from pprint import pprint
#socket.AI_CANONNAME: extract name of dns , and to verify if i use direct access to dns google or not
#AI_V4MAPPED dispay ips that we need to access to google (map of ip)
# objectif list of dns that help us to acces to dns google
info = socket.getaddrinfo('google.com','www',0,socket.SOCK_STREAM,0,socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME)
pprint(info)
