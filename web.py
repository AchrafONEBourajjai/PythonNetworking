from urllib.request import urlopen
response = urlopen('https://www.redhat.com')
# to get header from web sites and the function send request and get response from web site
print(response.readline()) #read <header></header>
print(response.url) #print the link of web site
print(response.read(140)) #set the quantity of information to read ex 140
print(response.read()) #read without quantity all html web site
print(response.status) # get the status of connection 200..etc from hhtp protocol mean okay importante to check
