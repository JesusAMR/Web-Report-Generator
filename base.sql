CREATE DATABASE Sigma;

USE Sigma;

/*Generar tabla de usuarios*/
CREATE TABLE Usuarios(
    id_Usuario INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nombre VARCHAR(15) NOT NULL,
    ap_Paterno VARCHAR(15) NOT NULL,
    ap_Materno VARCHAR(15) NOT NULL,
    fecha_Nacimiento date NOT NULL CHECK(fecha >= GETDATE()),
    contrasena VARCHAR(20) NOT NULL
);
/*Generar tabla de congeladores*/
CREATE TABLE Congelador(
    id_Congelador INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    temperatura_Normal_Min FLOAT NOT NULL,
    temperatura_Normal_Max FLOAT NOT NULL,
    humedad_Normal_Min FLOAT NOT NULL,
    humedad_Normal_Max FLOAT NOT NULL,
    capacidad INT NOT NULL,
    detalles VARCHAR(250),
    estado BOOLEAN NOT NULL
);
/*Generar tabla de lecturas*/
CREATE TABLE Lectura(
    id_Lectura INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    temperatura FLOAT NOT NULL,
    humedad FLOAT NOT NULL,
    corriente FLOAT 
);
/*Generar relacion lectura congelador*/
CREATE TABLE Lectura_Congelador(
    id_Lectura INT PRIMARY KEY REFERENCES Lectura(id_Lectura),
    id_Congelador INT NOT NULL REFERENCES Congelador(id_Congelador)
);

/* Ejemplo de como generar usuario*/
INSERT INTO Usuarios(nombre,ap_Paterno,ap_Materno,fecha_Nacimiento,contrasena) VALUES('jesus','miranda','rendon','1997-06-13',1234);