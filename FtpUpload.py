#upload data to the server
import  ftplib
import os # to use iostream to access to the file
ftpserver = "127.0.0.1"
fileupload = "anonymous.txt"
def ftpUpload(path,file_name):
    print("connecting to ftp server %s "%path)
    ftp = ftplib.FTP(path)
    external_file = os.path.split(file_name)[1]
    if external_file in (".txt",".doc",".html"): #for extension file
        ftp.storlines("STOR %s" %file_name,open(file_name))
    else:
        ftp.storbinary("STOR %s" %file_name,open(file_name,"rb"),1024)
    print("upload successfully %s " %file_name)

ftpUpload(ftpserver,fileupload)



