#!"C:\Python27\python.exe"

import mysql.connector
import cgi, cgitb 

db=mysql.connector.connect(user="jesus",passwd="1234",db="Sigma",unix_socket="/opt/lampp/var/mysql/mysql.sock")

cursor = db.cursor()

form = cgi.FieldStorage()

acceso = 0

User = form.getvalue("usuario")
Pass = form.getvalue("contrasena")

sql = """ SELECT nombre,contrasena FROM Usuarios WHERE nombre = '%s'""" % (User)

try:
	cursor.execute(sql)
	Results = cursor.fetchone()
	if(User == Results[0] and Pass == Results[1]):
		acceso = 1
except: 
	acceso = 0


#--------------------------------------------------------------------------------------------------------

print 'Content-type:text/html\r\n\r\n'
print '<html>'

print '<head> <title> Log In </title> </head>'

print '<body>'

if(acceso):
	print 'Usuario: %s <br/> Password: %s' % (User, Pass)
else:
	print Results
	print '<br>Usuario No Valido. Hay un error en su usuario o contrasena</br>'
	

print '</html>'

db.close()