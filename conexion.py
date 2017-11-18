import mysql.connector

class Conexion():
    credentials = {'user':'jesus','password':'1234','host':'localhost'}
    cnx = mysql.connector
    def connect(self):
        try:
            self.cnx = mysql.connector.connect(**self.credentials)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            self.cnx.close()
        print("Conectado")
    def close(self):
        self.cnx.close()
        print("Cerrado")


cn = Conexion()
cn.connect()
cn.close()