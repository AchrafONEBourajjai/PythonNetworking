import ipaddress as ip
net4 = ip.ip_network('192.168.1.0/24')
print(net4,net4.netmask)
net2 = net4.network_address
print(net2)
net3 = net4.broadcast_address
print(net3)
print(type(net2))