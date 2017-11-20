CREATE DATABASE Sigma;

USE [Sigma]

CREATE TABLE usuarios(
    id_Usuario INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
    nombre VARCHAR(15) NOT NULL,
    ap_Paterno VARCHAR(15) NOT NULL,
    ap_Materno VARCHAR(15) NOT NULL,
    fecha_Nacimiento date NOT NULL CHECK(fecha >= GETDATE()),
    contrasena VARCHAR(20) NOT NULL
)

CREATE TABLE refrigerador(
    id_Congelador INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
    temperatura_Normal_Min FLOAT NOT NULL,
    temperatura_Normal_Max FLOAT NOT NULL,
    humedad_Normal_Min FLOAT NOT NULL,
    humedad_Normal_Max FLOAT NOT NULL,
    capacidad INT NOT NULL,
    detalles VARCHAR(250) 
)