import nmap
import pprint #show info like a json obj
from pymongo import MongoClient
import json
def update_db(packet):
    client = MongoClient('localhost',27017)
    db = client['networkdata']
    collect = db['networkstatus']
    app_json = json.dumps(packet)
    collect.insert_one({"packet":app_json})


def scan_network():
    #scan a single host
    nm = nmap.PortScanner()
    scan_range = nm.scan(hosts="127.0.0.1")
    # scan_range = nm.scan(hosts="127.0.0.1 192.168.1.6 192.168.1.99") you can also scan more than host
    # scan_range = nm.scan(hosts="192.168.1.6-99") for range of ips
    # scan_range = nm.scan(hosts="192.168.1.0/24") for network
    data = scan_range['scan']
    pprint.pprint(data)
    update_db(data)

