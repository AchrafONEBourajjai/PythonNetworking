import urllib.error
from  urllib.request import urlopen
#how to manipulate error
# response.reason ====> ok,not found ...etc
try:
    response =urlopen('http://www.redhat.com/en1')
    print('status',response.status,response.reason )
except urllib.error.HTTPError as err :
    print('status',err.code,err.reason)
