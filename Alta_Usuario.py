#!"C:\Python27\python.exe"

import MySQLdb
import cgi, cgitb 

db=MySQLdb.connect(user="root",passwd="",db="SIGMA",unix_socket="/opt/lampp/var/mysql/mysql.sock")

cursor = db.cursor()

form = cgi.FieldStorage()

nombre = form.getvalue("nombre")
ap_Paterno = form.getvalue("ap_Paterno")
ap_Materno = form.getvalue("ap_Materno")
fecha_Nac = form.getvalue("fecha_Nac")
password = form.getvalue("contrasena")

sql = """ INSERT INTO Usuarios (nombre , ap_Paterno, ap_Materno, fecha_Nacimiento, contrasena) VALUES ('%s' , '%s' , '%s', '%s', '%s') """ % (nombre , ap_Paterno , ap_Materno, fecha_Nac, password)

try:
       cursor.execute(sql)
       db.commit()
except:
       db.rollback()

print 'Content-type:text/html\r\n\r\n'
print '<html>'

print '<head> <title> Alta de Usuario </title> </head>'

print '<body>'

print """

	<div align = 'center'> 	
	<h2> Usuario Agregado exitosamente </h2> 
	<br><a href = '/Sigma/menu.html'><input type = 'button' value = 'Menu' name = 'Menu'/> </a><br/>
	</div>

"""

print '</body>'

print '</html>'


