import mysql.connector
import random

def numAleatorio(min,max):
    rnd = random.uniform(min, max)
    return rnd

minTemp = -40.0
maxTemp = -10.0
minHum = 0.0
maxHum = 45.0
minCorr = 0
maxCorr = 5

congeladorID=1

db = mysql.connector.connect(user="jesus",passwd="1234",db="Sigma")
cursor = db.cursor()

insertar_Lectura = "INSERT INTO Lectura(temperatura, humedad, corriente) VALUES (%s, %s, %s)"
seleccionar_Lectura = "SELECT * FROM sigma.lectura WHERE FORMAT(temperatura,4) = FORMAT((%s),4) AND FORMAT(humedad,4) = FORMAT((%s),4) AND FORMAT(corriente,4) = FORMAT((%s),4)"
insertar_LectCong = "INSERT INTO Lectura_Congelador(id_Lectura, id_Congelador) VALUES (%s, %s)"
randTemp = numAleatorio(minTemp, maxTemp)
randHum = numAleatorio(minHum, maxHum)
randCorr = numAleatorio(minCorr, maxCorr)


randTemp = float("{0:.4f}".format(randTemp))
randHum = float("{0:.4f}".format(randHum))
randCorr = float("{0:.4f}".format(randCorr))
print randTemp
print randHum
print randCorr
informacion_Lectura = (randTemp, randHum, randCorr)

try:
    cursor.execute(insertar_Lectura, informacion_Lectura)
    db.commit()
except mysql.connector.Error as err:
    print err


try:
    cursor.execute(seleccionar_Lectura,informacion_Lectura)
    Results = cursor.fetchone()
    print Results
    id = int(Results[0])
except mysql.connector.Error as err:
    print err

informacion_LectCong = (id, congeladorID)

try:
    cursor.execute(insertar_LectCong, informacion_LectCong)
    db.commit()
except mysql.connector.Error as err:
    print err

cursor.close()
db.close()   
