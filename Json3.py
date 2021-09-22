import json
#json with set and tuples converted to list
s2 = ((10,20,30,40))
s3 = json.dumps(s2)
print(s3)
s4 = (('ab','cd','ef'))
s5 = json.dumps(s4)
print(s5)
s8 = json.loads(s5)
print(s8)
s6 = set(['ab','cd','ef'])
s7 = json.dumps(list(s6))
print(s6)
print(s7)
