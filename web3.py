#how to get headers from web site
from urllib.request import urlopen
from urllib.request import Request
import urllib.error
response = urlopen('http://www.redhat.com/en')
response1 = Request('http://www.redhat.com/en')
response1.add_header('Accept-Language','ar') #header key and value (http protocol)
print(response.getheaders()) #headers from http protocol
print(response.readlines()[:4]) # read header
