#!C:\Python27\python.exe

import mysql.connector

import cgi, cgitb 


#Conector a la base de datos con XAMPP
db = mysql.connector.connect(user="jesus",passwd="1234",db="Sigma")

cursor = db.cursor()

cursor.execute("SELECT VERSION();")

data = cursor.fetchone()

	
print "Content-Type: text/html"
print
print "<html>"
print """<!DOCTYPE html>
<html lang="es">
<head>"""
print '<title>Sigma Alimentos</title>'
print '</head>'
print '<body>'
print '<h3>Version de MySQL: %s</h3>' % (data)

print '<form action = "/Sigma/Check_Login.py" method = "post">'

print '<img src="Log_In.png" alt="Girl in a jacket" style="width:250px;height:250px;">'

print '<br/>User: <input type = "text" name = "User" required> <br/>'
print 'Password: <input type = "password" name = "Password" required> <br/>'
print '<input type = "submit" value = "Log in"> <br/>'

print '</form>'

print '</body>'
print '</html>'

#print "Version: %s" % data

db.close()

