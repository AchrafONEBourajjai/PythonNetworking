#how to code and decode json
import json
I = ['ali','ahmad','amine','achraf']
print(json.dumps(I))#dumps() converts objects to json string
s = json.dumps(I)
print(type(s)) #to know type of variable
s = '["ali","ahmad","amine","achraf"]'
print(json.loads(s)) #json object to list
print(json.loads(s)[3]) #prouve