import socket
def client(host,port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
    text = "this is broadcast message"
    sock.sendto(text.encode('ascii'),(host,port))
client("<broadcast>",6000)#<broadcast> or 192.168.1.255