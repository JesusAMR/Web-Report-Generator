import mysql.connector

class Conexion():
    credentials = {'user':'jesus','password':'1234','host':'localhost'}
    
    def __init__(self):
        cnx = mysql.connector.connect(**self.credentials)
        self.cursor = cnx.cursor()
    def query(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    