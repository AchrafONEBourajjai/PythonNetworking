import  os
import getpass
print(os.name.upper())
print(os.getgid())
print(os.getpid())
print(os.uname())
print(os.getuid())
p = getpass.getpass(prompt='what is you password ?')
if p.lower()=='cisco':
    print('right')
else:
    print('wrong')