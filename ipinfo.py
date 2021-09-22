import socket
import netifaces
hostname = socket.gethostname()
#ip_address = socket.gethostbyname(hostname)
#print("hostname is :",hostname)
ifaces = netifaces.interfaces() # return list of interfaces in your computer
print(ifaces)
for iface in ifaces:
    ipaddr = netifaces.ifaddresses(iface) # return dictionary that contains adress,netmask
    #print(ipaddr)
    if netifaces.AF_INET in ipaddr: #just ipv4 info
        ipadd=ipaddr[netifaces.AF_INET]
        print(ipadd)
        ipadd=ipadd[0]
        print("Network Interface: {}".format(iface))
        print(("\t address: {}".format(ipadd['addr'])))
        print(("\t Mask: {}".format(ipadd['netmask'])))
gateway = netifaces.gateways()
print("Default gateway {}".format(gateway['default'][netifaces.AF_INET][0]))