#how to connect url
from urllib.parse import urlsplit
url1 = urlsplit("https://www.google.com/search?q=supmaroc+&source=hp&ei=fnsSYd6JLpOU1fAPkaKAgAE&iflsig=AINFCbYAAAAAYRKJjjyVhtbukLeYMnASy4uznEITrZY4&oq=supmaroc+&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOhQILhCABBDHARCjAhCLAxCoAxCnAzoXCC4QgAQQxwEQowIQiwMQpwMQqAMQkwI6BQguEIAEOhQILhCABBDHARCjAhCLAxCnAxCoAzoICC4QgAQQkwI6FAguEIAEEMcBEK8BEIsDEKYDEKgDOhYILhCABBDHARCvARAKEIsDEKYDEKgDOgcIABCABBAKUJICWIAkYLolaABwAHgAgAGRAogB_QuSAQUwLjguMZgBAKABAbgBAg&sclient=gws-wiz&ved=0ahUKEwjewIunxKbyAhUTShUIHRERABAQ4dUDCAY&uact=5") #urlsplit(): to devide url to parts
url2 = tuple(url1)
#info to extract
print(url2)
print(url1.scheme)
print(url1.netloc)
print(url1.path)
print(url1.query)
print(url1.fragment)
print(url1.hostname)
print(url1.password)


