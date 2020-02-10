
from ftplib import FTP

def ftpconnect(host, username, password):
	ftp = FTP()
	ftp.set_debuglevel(2)
	ftp.connect(host, 21) #(host, port)
	ftp.login(username, password)
	
def downloadfile(ftp, remotepath, localpath):
	bufsize = 1024
	fp = open(localpath, 'wb')
	ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
	ftp.set_debuglevel(0)
	fp.close()
	
def uploadfile(ftp, remotepath, localpath):
	bufsize = 1024
	fp = open(localpath, 'rb')
	ftp.retrbinary('STOR ' + remotepath, fp, bufsize)
	ftp.set_debuglevel(0)
	fp.close()
	
if __name__ == "__main__":
	ftp = ftpconnect("10.10.15.70", "arc1", "arc10000") #(host, account, password)
	# downloadfile(ftp, "XXX", "XXX")
	filename = "ECP.py"
	uploadfile(ftp, "/Installer/{0}".format(filename), filename)
	
	ftp.quit()
