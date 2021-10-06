import nmap
nm = nmap.PortScanner()
nm.scan('192.168.1.1','1-1024','-v')
print(nm.scaninfo())
print(nm.csv())