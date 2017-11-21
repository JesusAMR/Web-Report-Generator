#!"C:\Python27\python.exe"

import MySQLdb
import cgi, cgitb 

db=MySQLdb.connect(user="root",passwd="",db="SIGMA")

cursor = db.cursor()

form = cgi.FieldStorage()

ID = form.getvalue("ID")
fecha_Nac = form.getvalue("fecha_Nac")

acceso = 0

sql = """SELECT * FROM usuarios WHERE id_Usuario = '%s'""" % (ID)

cursor.execute(sql)
Results = cursor.fetchone()

if(Results):
	acceso = 1

#try:
	#cursor.execute(sql)
	#Results = cursor.fetchone()

sql = """DELETE FROM Usuarios WHERE id_Usuario = '%s'""" % (ID)

print 'Content-type:text/html\r\n\r\n'
print '<html>'

print '<head> <title> Baja de Usuario </title> </head>'

print '<body>'

try:
	cursor.execute(sql)
	db.commit()

	if(acceso == 1):

		print """
			<div align = 'center'> 	
			<h2> Usuario Eliminado Exitosamente </h2> 
			<br><a href = '/Sigma/menu.html'><input type = 'button' value = 'Menu' name = 'Menu'/> </a><br/>
			</div>
		""" 
	else:
		print """
			<div align = 'center'> 	
			<h2> Usuario No Encontrado </h2> 
			<br><a href = '/Sigma/menu.html'><input type = 'button' value = 'Menu' name = 'Menu'/> </a><br/>
			</div>
		""" 

except:
	db.rollback()

print '</body>'
print '</html>'