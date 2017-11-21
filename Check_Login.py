#!"C:\Python27\python.exe"

import MySQLdb
import cgi, cgitb 

db=MySQLdb.connect(user="root",passwd="",db="SIGMA",unix_socket="/opt/lampp/var/mysql/mysql.sock")

cursor = db.cursor()

form = cgi.FieldStorage()

acceso = 0

ID = form.getvalue("id")
Pass = form.getvalue("contrasena")

sql = """SELECT * FROM usuarios WHERE id_Usuario = '%s'""" % (ID)

try:
	cursor.execute(sql)
	Results = cursor.fetchone()
	if(ID == str(Results[0]) and Pass == Results[5]):
		acceso = 1
except: 
	acceso = 0


#--------------------------------------------------------------------------------------------------------

print 'Content-type:text/html\r\n\r\n'
print '<html>'

print '<head> <title> Log In </title> </head>'

print '<body>'

if(acceso):
	print '<meta http-equiv="refresh" content="0; url=/Sigma/menu.html" />'
else: 
	print '<body>Usuario No Valido. Hay un error en su User o Password</body>'
	print '<meta http-equiv="refresh" content="0; url=/Sigma/Login.html" />'

print '</html>'

db.close()