CREATE DATABASE Sigma;

USE [Sigma]

CREATE TABLE Usuarios(
    id_Usuario INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
    nombre VARCHAR(15) NOT NULL,
    ap_Paterno VARCHAR(15) NOT NULL,
    ap_Materno VARCHAR(15) NOT NULL,
    fecha_Nacimiento date NOT NULL CHECK(fecha >= GETDATE()),
    contrasena VARCHAR(20) NOT NULL
)

CREATE TABLE Congelador(
    id_Congelador INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
    temperatura_Normal_Min FLOAT NOT NULL,
    temperatura_Normal_Max FLOAT NOT NULL,
    humedad_Normal_Min FLOAT NOT NULL,
    humedad_Normal_Max FLOAT NOT NULL,
    capacidad INT NOT NULL,
    detalles VARCHAR(250),
    estado BOOLEAN NOT NULL
)

CREATE TABLE Lectura(
    id_Lectura INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
    temperatura FLOAT NOT NULL,
    humedad FLOAT NOT NULL,
    corriente FLOAT 
)

CREATE TABLE Lectura_Congelador(
    id_Lectura INT PRIMARY KEY FOREIGN KEY REFERENCES Lectura(id_Lectura),
    id_Congelador INT FOREIGN KEY REFERENCES Congelador(id_Congelador)
)

