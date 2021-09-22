import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.connect(("127.0.0.1",3000))
text = "im client"
data = text.encode('ascii')
delay = 0.1
while (True):
    sock.send(data)
    print("waiting {}".format(delay))
    sock.settimeout(delay)
    try:
        sock.recv(1024)
    except socket.timeout as exc:
        delay*=2
        if delay > 3.0:
            raise  RuntimeError("maybe server is down") from exc
    else:
        break
print("The server says {}".format(data.decode('ascii')))