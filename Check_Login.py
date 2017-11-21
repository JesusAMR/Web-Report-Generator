#!"C:\Python27\python.exe"

import mysql.connector
import cgi, cgitb 

db=mysql.connector.connect(user="jesus",passwd="1234",db="Sigma")

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


print 'Content-type:text/html\r\n\r\n'
print '<html>'

print '<head> <title> Log In </title> </head>'

print '<body>'
print "<div align='center'>"
if(acceso):
	print '<meta http-equiv="refresh" content="0; url=/Sigma/html/Menu.html" />'	
else:
	print '<meta http-equiv="refresh" content="0; url=/Sigma/html/Login.html" />'
	print '<br>Usuario No Valido. Hay un error en su usuario o contrasena</br>'
	
print "</div>"
print '</html>'

db.close()