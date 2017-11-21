#!"C:\Python27\python.exe"

import mysql.connector
import cgi
import cgitb

db= mysql.connector.connect(user="jesus",passwd="1234",db="Sigma")
cursor = db.cursor()
form = cgi.FieldStorage()
ID = form.getvalue("ID")
acceso = 0

selCongelador = """SELECT * FROM Congelador WHERE id_Congelador = '%s' """ % (ID)
elCongelador = """DELETE FROM Congelador WHERE id_Congelador = '%s'""" % (ID)
cursor.execute(selCongelador)
Results = cursor.fetchone()

if(Results):
	acceso = 1

print 'Content-type:text/html\r\n\r\n'
print '<html>'

print '<head> <title> Baja de Congelador </title> </head>'

print '<body>'

try:
	cursor.execute(elCongelador)
	db.commit()

	if(acceso == 1):

		print """
			<div align = 'center'> 	
			<h2>Congelador Eliminado Exitosamente </h2> 
			<br><a href = '/Sigma/html/menu.html'><input type = 'button' value = 'Menu' name = 'Menu'/> </a><br/>
			</div>
		""" 
	else:
		print """
			<div align = 'center'> 	
			<h2> Congelador No Encontrado </h2> 
			<br><a href = '/Sigma/html/menu.html'><input type = 'button' value = 'Menu' name = 'Menu'/> </a><br/>
			</div>
		""" 

except:
	db.rollback()

print '</body>'
print '</html>'
cursor.close()
db.close()