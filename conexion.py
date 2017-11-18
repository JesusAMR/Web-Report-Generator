import mysql.connector

class Conexion():
    credentials = {'user':'jesus','password':'1234','host':'localhost'}
    def __init__():

    def connect():
        try:
            cnx = mysql.connector.connect(**credentials)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.close()
    def close():
        cnx.close()

