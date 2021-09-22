import http.client,urllib.parse
con = http.client.HTTPSConnection('www.facebook.com')
con.request('HEAD','/')
res = con.getresponse()
print(res.status,res.reason)
data = res.read()
print(len(data))
param = urllib.parse.urlencode({'@number':12345,'@type':'issue','@action':'show'})
headers = {"Content-type":"application/x-form-urlencoded","Accept":"text/plain"}
#send POST to web site
con = http.client.HTTPConnection("bugs.python.org")
con.request('POST',"",param,headers)
response = con.getresponse()
print(response.status,response.reason)
data = response.read()
print(data)