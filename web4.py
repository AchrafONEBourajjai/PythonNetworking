from urllib.request import urlopen
res = urlopen('https://www.python.org')
format,params = res.getheader('Content-Type').split(';') #Content-Type from header
print(res.getheader('Content-Type'))
print('',format,params)
charset= params.split('=')[0]
print(charset)
content = res.read().decode('utf-8')#to decode byte with utf-8 content
print(content)