import socket
from pprint import pprint
sock1 = socket.gethostname() # localy
sock2 = socket.getfqdn()# localy
sock3=socket.gethostbyname('google.com')#internet
sock4=socket.gethostbyaddr('google.com')#internet the original one
sock5=socket.getprotobyname('TCP')#port number
sock6=socket.getservbyport(80)#name of protocol
sock7=socket.getservbyname('www')#port of protocol
pprint(sock1)
pprint(sock2)
pprint(sock3)
pprint(sock4)
pprint(sock5)
pprint(sock6)
pprint(sock7)