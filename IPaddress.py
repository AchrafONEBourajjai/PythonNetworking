import socket
if __name__=='__main__':
    hostname='www.google.com'
    ipaddresse=socket.gethostbyname(hostname)
    print(f"ip is {ipaddresse} addresse is {hostname}")