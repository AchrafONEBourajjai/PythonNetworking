import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.1.3','22','admin','admin')
stdin , stdout,stderr = client.exec_command('ip address print')
for line in stdout :
    print(line.strip('\n'))
client.close()
