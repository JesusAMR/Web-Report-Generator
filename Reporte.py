#!"C:\Python27\python.exe"

import mysql.connector
import cgi, cgitb

db = mysql.connector.connect(user="jesus",passwd="1234",db="Sigma")
cursor = db.cursor()
form = cgi.FieldStorage()

temperatura = []
humedad = []
corriente = []
valido = False
clave = form.getvalue("clave")
seleccionar_Congelador = "SELECT * FROM congelador WHERE id_Congelador = '%s' "% (clave)
seleccionar_LecturasCong = "SELECT * FROM lectura_congelador as T2 INNER JOIN lectura  AS T1 ON T1.id_Lectura = T2.id_Lectura WHERE T2.id_Congelador = '%s' " % (clave)

try:
    cursor.execute(seleccionar_Congelador)
    results = cursor.fetchone()
    valido = True
except mysql.connector.Error as err:
    print err

print "Content-Type: text/html"
print
print "<html>"
print """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="/Sigma/html/Estilo.css">
    <style>
		table, th, td {
		    border: 1px solid black;
		    border-collapse: collapse;
		    background-color: #cccc99;
		}
	</style>
</head>"""
print "<body>"
if valido:
    try:
        cursor.execute(seleccionar_LecturasCong, clave)
        results = cursor.fetchall()
    except mysql.connector.Error as err:
        print err
for res in results:
    temperatura.append(res[3])
    humedad.append(res[4])
    corriente.append(res[5])
print "<div align = 'center'> "
print "<img src='/Sigma/html/logo.svg' style='width:250px;height:225px;'><br>"
print "<h2> Congelador %s </h2><br>	</div>"%(clave)
print """
	<table style="width:100%">
  	<tr>
    <th>Temperatura (C)</th>
    <th>Humedad (%)</th>
    <th>Corriente (A)</th>
    </tr>	
"""

for i in range(0,len(temperatura)):
	print """

		<tr>
	    <td align = 'center'>%f</td>
	    <td align = 'center'>%f</td>
	    <td align = 'center'>%f</td>
	 	</tr>

	""" % (temperatura[i] , humedad[i] , corriente[i])

print"</body>"
print"</html>"