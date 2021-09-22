import socket
buffersize=2048
def server(host,port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((host,port))
    print(f'listening to {sock.getsockname()}')
    while True:
        data,address = sock.recvfrom(buffersize)
        text = data.decode('ascii')
        print(f"The client {address} says {text} ")
server('',6000)