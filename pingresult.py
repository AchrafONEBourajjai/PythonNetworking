import subprocess
with open('myfile.txt','w') as myfile:
    for i in range(1,10):
        ip = f"192.168.1.{i}"
        result = subprocess.call(['ping',ip],stdout=myfile,stderr=myfile)
        if result==True:
            print(ip,result)
        else :
            print(ip,result)
