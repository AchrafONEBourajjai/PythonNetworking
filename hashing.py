import  hashlib
a = hashlib.sha224(b"my name is abl").hexdigest()
print(a)
#hashing file
blocksize = 65535
hasher = hashlib.md5()
with open("image.jpg","rb") as fl:
    buffer = fl.read(blocksize)
    while len(buffer) > 0 :
        hasher.update(buffer)
        buffer = fl.read(blocksize)
print(hasher.hexdigest())
