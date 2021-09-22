#retrieve data from ftp server
import ftplib
ftp_server = "ftp.redhat.com"
def clientFtpConnection(path,username,email):
    ftp = ftplib.FTP(path,username,email) #for open the connection
    ftp.cwd('redhat')#specefie directory into server 'redhat' name of directory
    print("File list at %s :",path)
    files = ftp.dir() #to enter to the directory
    print(files) #show all directory into redhat dir
    ftp.close()
clientFtpConnection(path=ftp_server,username="anonymous",email="nobody@nourl.com")
