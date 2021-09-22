import socket
from datetime import datetime
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for i in range(5):
    text = 'time is : {}\n'.format(datetime.now())
    data = text.encode('ascii')
    sock.sendto(data,('127.0.0.1',3000))
    data,address = sock.recvfrom(1024)
    text = data.decode('ascii')
    print('client use {}\n'.format(sock.getsockname()))
    print("server {} replied: {}\n".format(address,text))