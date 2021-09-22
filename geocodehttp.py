import json
from urllib.parse import quote_plus
import http.client
def geocode(addr):
    base='/maps/api/geocode/json'
    path=f'{base}?address={quote_plus(addr)}&sensor=false'
    connection = http.client.HTTPConnection('maps.google.com')
    connection.request('GET',path)
    reply = connection.getresponse().read()
    reply2 = json.loads(reply.decode('utf-8'))
    print(reply2)

if __name__=='__main__':
    geocode('angle boulevard mohamed VI et al hizam')
