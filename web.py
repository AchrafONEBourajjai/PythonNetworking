from urllib.request import urlopen
res = urlopen('https://www.wikipedia.org')
print(res.read())
