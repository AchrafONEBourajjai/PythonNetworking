import subprocess
com = subprocess.call(["ls","-al"])
print(com)
process = subprocess.Popen(['notepad++','test.txt'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
stdout,stderr=process.communicate()
print(stdout)