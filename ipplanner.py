import ipaddress as ip
CLASS_C_ADDR ='192.168.1.0'
if __name__=='__main__':
    not_config = True
    while not_config:
        prefix = input("Enter the prefix (24-30) : ")
        prefix = int(prefix)
        if prefix not in range (23,31):
            raise Exception ("Prefix must be between range (24-30)")
        net_addr = CLASS_C_ADDR+ '/' +str(prefix)
        print("network address : %s"%net_addr)
        try:
            network = ip.ip_network(net_addr)
        except:
            raise  Exception("Failed to create network")
        print("This is prefix will give %s IP addresses"%network.num_addresses)
        print("Network configuration will be like this :")
        print("\t Network addresse: %s"%str(network.netmask))
        print("\t broadcast addresse : %s "%str(network.broadcast_address))
        firstip,lastip = list(network.hosts())[0],list(network.hosts())[-1]
        print("\t host ip adresses : from %s to %s "%(firstip,lastip))
        status = input('Is this configuration okay [Y/N]')
        status = status.lower()
        if status.strip()=='y':
            not_config=False
        else:
            not_config=True



