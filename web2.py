import urllib.error
from urllib.request import urlopen
try:
    response = urlopen('http://www.redhat.com/en1')
    print('status %s %s'%(response.status,response.reason))
except urllib.error.HTTPError as err:
    print('status: %s reason: %s url: %s'%(err.status,err.reason,err.url))