import socket
from urllib.parse import  quote_plus
def geocode(addr):
    request_text=""""\
    GET /maps/api/geocode/json?address={}&sensor=false HTTP/1.1\r\n\
    Host:maps.google.com:80\r\n\
    User-Agent:main.py
    Connection:close\r\n\
    """
    sock=socket.socket()
    sock.connect(('maps.google.com',80))
    request=request_text.format(quote_plus(addr))
    reply=b''
    sock.sendall(request.encode('ascii'))
    while True:
        data = sock.recv(4096)
        if not data:
            break
        reply+=data
    print(reply.decode('utf-8'))
