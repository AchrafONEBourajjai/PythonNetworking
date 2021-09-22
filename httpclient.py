import requests
from urllib.request import urlopen
import  urllib.error
try:
    r = urlopen('https://www.python.org')
    print(r.read()) #byte
except urllib.error as err:
    print(r.read(),err)
#or methode 2
r = requests.get('https://www.google.com/headers') # we can use it with headers or not
print(r.text)
