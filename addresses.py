import  ipaddress
import binascii
ADDRESSES = [
    '10.9.0.6',
    'fdfd:87b5:b475:be3e:b1bc:e121:a8eb:14aa',
]
for ip in ADDRESSES :
    addr = ipaddress.ip_address(ip)
    print("{!r}".format(addr))
    print("IP Version:",addr.version)
    print("is private:",addr.is_private)
    print("packed from:",binascii.hexlify(addr.packed))
    print("integer ",int(addr))
print()
NETWORKS = [
    '10.9.0.0/24',
    'fdfd:87b5:b475:be3e::/64',
]
for n in NETWORKS :
    net = ipaddress.ip_network(n)
    print("{!r}".format(net))
    print("is private:", net.is_private)
    print("broadcast:", net.broadcast_address)
    print("compressed:",net.compressed)
    print("with netmask:",net.with_netmask)
    print("with hostmask:",net.with_hostmask)
    print("num addresses:",net.num_addresses)
print()

