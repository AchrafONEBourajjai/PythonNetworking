import  http.client
con = http.client.HTTPSConnection('www.python.org') #make connection
con.request('GET','/') #(type:get or post , query)
r=con.getresponse() # response from the web site
print(r.status,r.reason)
while not r.closed:
    print(r.read(200))