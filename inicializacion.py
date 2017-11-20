from conexion import Conexion
import mysql.connector

DBNAME = 'TEST_1'
credentials = {'user':'jesus','password':'1234','host':'localhost'}
cnx = mysql.connector.connect(**credentials)
cursor = cnx.cursor()
cursor.execute("CREATE DATABASE {}".format(DBNAME))