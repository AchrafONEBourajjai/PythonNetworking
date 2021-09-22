#python 2.7
import socket
from geoip import geolite2

hostname = 'amazon.co.uk'
ipaddr = socket.gethostbyname(hostname)
print("IP Addresse : {} ".format(ipaddr))
m = geolite2.lookup(ipaddr)
if m is not None:
    print(m.country)
    print(m.continent)
    print(m.timezone)
    print(m.subdivisions)
    print(m.location)