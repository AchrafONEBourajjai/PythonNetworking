import json
#json  with dictionary
s = json.dumps({'AL':'ali','AH':'ahmad','AM':'amine','AC':'achraf'}) #dictionary to json string
print(s)
print(type(s))
# json can also use nestedobject
s2 = {'AL':['info','elect'],'AH':['info','biologie'],'AM':['info','geology'],'AC':['info','agrobiology']}
print(json.dumps(s2))
s3 = {10:100,20:200,30:300,40:400}
print(json.dumps(s3))