import  ipaddress as ip
net4 = ip.ip_network('192.168.1.0/24')
addr = net4.network_address
mask = net4.netmask
broadcast = net4.broadcast_address
addressesnum = net4.num_addresses
print(addr,mask,broadcast,addressesnum)
available_hosts = list(net4.hosts())
length = len(available_hosts)
print(available_hosts,length)
#show subnet
subnets1 = net4.subnets()
subnets1 = list(subnets1)
print(subnets1)
#super subnet or parent subnet
superSubnet = net4.supernet()
print(superSubnet)