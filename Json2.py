import json
s2 = {10:100,20:200,30:300,40:400}
s3 = json.dumps(s2)
print(s3) #the keys is always String to python
s4 = json.loads(s3)
print(s4)#the keys is always String to python
s5 = {int(key):val for key,val in s4.items()} #now keys are converted to int type, value is already in int type
print(s5)