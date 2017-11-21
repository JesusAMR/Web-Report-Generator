#!"C:\Python27\python.exe"

import mysql.connector
import cgi
import cgitb 

db = mysql.connector.connect(user="jesus",passwd="1234",db="Sigma")

cursor = db.cursor()
form = cgi.FieldStorage()

clave = int(form.getvalue("clave"))
tempMinimo  = float(form.getvalue("temp-min"))
tempMaximo  = float(form.getvalue("temp-max"))
humMinimo = float(form.getvalue("hum-min"))
humMaximo = float(form.getvalue("hum-max"))
capacidad = int(form.getvalue("capacidad"))
estado = int(form.getvalue("estado"))
detalles = form.getvalue("detalles")

if not detalles:
    detalles = " "
else:
    pass

anadir_congelador =    ("INSERT INTO Congelador "
                            "(id_Congelador,temperatura_Normal_Min,temperatura_Normal_Max,humedad_Normal_Min,humedad_Normal_Max,capacidad,detalles,estado)" "values(%s, %s, %s, %s, %s, %s, %s, %s)")

informacion_congelador = (clave, tempMinimo, tempMaximo, humMinimo, humMaximo, capacidad, detalles, estado)

print "Content-Type: text/html"
print
print "<html>"
print """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="Estilo.css">
</head>"""
print "<body>"
print "<div align='center'>"
try:
    cursor.execute(anadir_congelador, informacion_congelador)
    db.commit()
    print "<h2> Congelador agregado exitosamente </h2>"
    print "<br><a href = '/Sigma/html/menu.html'><input type = 'button' value = 'Menu' name = 'Menu'/> </a><br/>"
except mysql.connector.Error as err:
    print err
    print "<h2> Congelador no agregado</h2>"
    print "<br><a href = '/Sigma/html/menu.html'><input type = 'button' value = 'Menu' name = 'Menu'/> </a><br/>"
print "</div>"
print"</body>"
print"</html>"

cursor.close()
db.close()